"""
Bean There Done That - analysis + deck builder.

Reads the case dataset, computes every KPI used in the pitch, and injects the
results into deck_template.html. Produces two files in ../ :

  Bean_There_Pitch.html          loads Plotly from the cdnjs CDN (small file)
  Bean_There_Pitch_offline.html  Plotly embedded, works without internet

Run:  python build_deck.py
Needs: pandas, openpyxl, numpy
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
XLSX = ROOT / "Bean there done that data.xlsx"
OUT = HERE.parent

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
MON = [m[:3] for m in MONTHS]
ROASTS = ["Light", "Medium", "Dark"]
M_IDX = {m: i + 1 for i, m in enumerate(MONTHS)}

# Approximate population per province, CBS 1 Jan 2023 (thousands)
POPULATION = {
    "Groningen": 596, "Friesland": 659, "Drenthe": 499, "Overijssel": 1184,
    "Flevoland": 444, "Gelderland": 2133, "Utrecht": 1388,
    "Noord-Holland": 2953, "Zuid-Holland": 3804, "Zeeland": 391,
    "Noord-Brabant": 2626, "Limburg": 1118,
}
# Dutch public holidays 2023 on which PostNL does not deliver
HOLIDAYS = pd.to_datetime(["2023-01-02", "2023-04-07", "2023-04-10", "2023-04-27",
                           "2023-05-18", "2023-05-29", "2023-12-25", "2023-12-26",
                           "2024-01-01"])
NAMEPLATE = {"Probat P60": 215, "Probat Px120": 480}  # kg/h, from case brief
CONTAINER_KG = 12 * 12 * 70  # 12 pallets x 12 bags x 70 kg


def r(x, n=1):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), n)


def lst(s, n=1):
    return [r(v, n) for v in s]


def load():
    x = pd.read_excel(XLSX, sheet_name=None)
    clean = {}
    for k, d in x.items():
        clean[k] = d.loc[:, ~d.columns.astype(str).str.startswith("Unnamed")]
    return clean


def main():
    x = load()
    raw = x["Inventory (raw material)"].copy()
    fin = x["Inventory (finished product)"].copy()
    rst = x["Roasting"].copy()
    eco = x["E-com sales orders by product"].copy()
    b2b = x["B2B orders"].copy()

    # ---------- normalise ----------
    for d in (raw, fin, rst):
        d["m"] = d["Month"].map(M_IDX)
    fin["roast"] = fin["Product"].str.split().str[0].str.capitalize()
    rst["roast"] = rst["Product type"].str.split().str[0].str.capitalize()
    eco["roast"] = eco["Product"].str.split().str[0]
    eco["kg"] = eco["Quantity"] * np.where(eco["Bag type"] == 1, 1.0, 0.5)
    eco["m"] = eco["Order date"].dt.month
    b2b["roast"] = "Medium"
    b2b["kg"] = b2b["Quantity"].astype(float)  # bag type 1 = 1 kg
    b2b["m"] = b2b["Delivery date"].dt.month

    D = {"months": MON}

    # ---------- demand ----------
    demand = pd.concat([eco[["m", "roast", "kg"]], b2b[["m", "roast", "kg"]]])
    dem = demand.pivot_table(index="m", columns="roast", values="kg", aggfunc="sum")
    eco_kg = eco.pivot_table(index="m", columns="roast", values="kg", aggfunc="sum")
    b2b_kg = b2b.groupby("m")["kg"].sum()
    daily = eco.groupby("Order date").agg(orders=("kg", "size"), kg=("kg", "sum"))
    mon = eco.groupby("m").agg(orders=("kg", "size"), kg=("kg", "sum"),
                               rev=("Value", "sum"), aov=("Value", "mean"),
                               days=("Order date", "nunique"))
    mon["orders_per_day"] = mon.orders / mon.days
    mon["kg_per_order"] = mon.kg / mon.orders
    D["demand"] = {k: lst(dem[k], 0) for k in ROASTS}
    D["demand_total"] = lst(dem.sum(axis=1), 0)
    D["ecom_kg_total"] = lst(eco_kg.sum(axis=1), 0)
    D["b2b_kg"] = lst(b2b_kg, 0)
    D["orders_per_day"] = lst(mon.orders_per_day, 1)
    D["kg_per_order"] = lst(mon.kg_per_order, 2)
    D["aov"] = lst(mon.aov, 2)
    D["daily"] = {"date": [d.strftime("%Y-%m-%d") for d in daily.index],
                  "orders": daily.orders.astype(int).tolist(),
                  "kg": lst(daily.kg, 0)}

    # ---------- production / roasting ----------
    rst["batches"] = rst["Number of batches per day"] * rst["Workdays"]
    rst["rejected"] = rst["Total rejected batches p/month"]
    rst["good"] = rst.batches - rst.rejected
    rst["in_kg"] = rst.batches * rst["Load weight p/batch"]
    rst["out_kg"] = rst.good * rst["Final weight /pbatch"]
    rst["rej_kg"] = rst.rejected * rst["Final weight /pbatch"]
    rst["shrink"] = 1 - rst["Final weight /pbatch"] / rst["Load weight p/batch"]
    rst["cycle"] = rst["Setup time p/batch"] + rst["Run time p/batch (m)"]
    rst["roast_min_day"] = rst["Number of batches per day"] * rst.cycle
    rst["pack_min_day"] = rst["Number of batches per day"] * rst["Packing time p/batch"]
    prod = rst.pivot_table(index="m", columns="roast", values="out_kg", aggfunc="sum")
    D["production"] = {k: lst(prod[k], 0) for k in ROASTS}
    D["production_total"] = lst(prod.sum(axis=1), 0)
    D["workdays"] = rst.groupby("m")["Workdays"].first().astype(int).tolist()

    mach = rst.groupby(["Machine", "m"]).agg(roast_min=("roast_min_day", "sum"),
                                             pack_min=("pack_min_day", "sum")).reset_index()
    D["machine_min_day"] = {mc: lst(g.roast_min, 0) for mc, g in mach.groupby("Machine")}
    D["packing_min_day"] = lst(mach.groupby("m").pack_min.sum(), 0)

    machines = []
    for mc, g in rst.groupby("Machine"):
        hours = (g.batches * g.cycle).sum() / 60
        kg_in = g.in_kg.sum()
        machines.append({
            "machine": mc,
            "nameplate_kgph": NAMEPLATE[mc],
            "actual_kgph": r(kg_in / hours, 0),
            "effectiveness": r(kg_in / hours / NAMEPLATE[mc] * 100, 0),
            "setup_share": r((g.batches * g["Setup time p/batch"]).sum() / (g.batches * g.cycle).sum() * 100, 0),
            "avg_setup": r((g.batches * g["Setup time p/batch"]).sum() / g.batches.sum(), 1),
            "avg_run": r((g.batches * g["Run time p/batch (m)"]).sum() / g.batches.sum(), 1),
            "roast_hours_day": r(mach[mach.Machine == mc].roast_min.mean() / 60, 2),
            "load_fill": r(g["Load weight p/batch"].mean() / (60 if mc.endswith("P60") else 120) * 100, 0),
            "out_kg": r(g.out_kg.sum(), 0),
            "out_kg_per_roast_hour": r(g.out_kg.sum() / hours, 1),
        })
    D["machines"] = machines

    by_roast = rst.groupby("roast").agg(batches=("batches", "sum"), rejected=("rejected", "sum"),
                                        rej_kg=("rej_kg", "sum"),
                                        w=("QC fail/ Weight", "sum"), c=("QC fail/ Color", "sum"),
                                        p=("QC fail/ Roast profile", "sum"),
                                        shrink=("shrink", "mean"))
    by_roast["rate"] = by_roast.rejected / by_roast.batches * 100
    D["quality"] = {k: {"batches": r(by_roast.loc[k, "batches"], 0),
                        "rejected": int(by_roast.loc[k, "rejected"]),
                        "rate": r(by_roast.loc[k, "rate"], 1),
                        "rej_kg": r(by_roast.loc[k, "rej_kg"], 0),
                        "weight": int(by_roast.loc[k, "w"]), "colour": int(by_roast.loc[k, "c"]),
                        "profile": int(by_roast.loc[k, "p"]),
                        "shrink": r(by_roast.loc[k, "shrink"] * 100, 1)} for k in ROASTS}
    rej_m = rst.assign(rate=rst.rejected / rst.batches * 100).pivot_table(
        index="m", columns="roast", values="rate", aggfunc="sum")
    D["reject_rate_month"] = {k: lst(rej_m[k], 1) for k in ROASTS}

    # ---------- finished goods ----------
    fs = fin.pivot_table(index="m", columns="roast", values="Stock level", aggfunc="sum")
    fx = fin.pivot_table(index="m", columns="roast", values="Scrapped", aggfunc="sum").abs()
    fv = fin.pivot_table(index="m", columns="roast", values="Stock value", aggfunc="sum")
    price = fin.groupby("roast")["Unit price"].first()
    D["fg_stock"] = {k: lst(fs[k], 0) for k in ROASTS}
    D["fg_scrap"] = {k: lst(fx[k], 0) for k in ROASTS}
    D["fg_value"] = lst(fv.sum(axis=1), 0)
    cover = fs / dem * 30.4  # days of demand in stock
    D["fg_cover_days"] = {k: lst(cover[k], 0) for k in ROASTS}
    scrap_kg = fx.sum().sum()
    scrap_eur = sum(fx[k].sum() * price[k] for k in ROASTS)

    # ---------- green beans ----------
    gb = raw[raw.Unit == "Kg"].copy()
    gb["origin"] = gb.Product.str.extract(r"COO (.+)\)")[0]
    gs = gb.pivot_table(index="m", columns="origin", values="Stock level")
    gp = gb.pivot_table(index="m", columns="origin", values="Purchased")
    gx = gb.pivot_table(index="m", columns="origin", values="Scrapped")
    use = -(gs.diff() - gp - gx)  # consumption implied by stock movement
    avg_use = use.mean()
    D["green_stock"] = {o: lst(gs[o], 0) for o in gs.columns}
    D["green_cover_days"] = {o: lst(gs[o] / avg_use[o] * 30.4, 0) for o in gs.columns}
    D["green_total_cover_days"] = lst(gs.sum(axis=1) / avg_use.sum() * 30.4, 0)
    D["green_price"] = gb.groupby("origin")["Unit price"].first().round(2).to_dict()
    D["green_purchased_kg"] = r(gp.sum().sum(), 0)
    D["green_scrapped_kg"] = r(gx.sum().sum() * -1, 0)
    D["green_use_month"] = r(avg_use.sum(), 0)
    green_cost = (gp.sum() * gb.groupby("origin")["Unit price"].first()).sum()
    avg_green_price = green_cost / gp.sum().sum()

    # ---------- delivery ----------
    bd = pd.offsets.CustomBusinessDay(holidays=HOLIDAYS)
    promise = pd.Series(pd.DatetimeIndex(eco["Order date"]) + bd, index=eco.index)
    eco["late"] = (eco["Delivery date"] - promise).dt.days > 0
    eco["lead"] = (eco["Delivery date"] - eco["Order date"]).dt.days
    D["ontime_month"] = lst((1 - eco.groupby("m").late.mean()) * 100, 1)
    D["lead_dist"] = eco.lead.value_counts().sort_index().astype(int).to_dict()
    D["deliveries_weekday"] = eco["Delivery date"].dt.dayofweek.value_counts().sort_index().astype(int).tolist()

    # ---------- shipping economics ----------
    bands = [0, 30, 55, 80, 110, 200]
    labels = ["< €30", "€30–55", "€55–80", "€80–110", "> €110"]
    eco["band"] = pd.cut(eco.Value, bands, labels=labels, right=False)
    sb = eco.groupby("band", observed=True).agg(orders=("Value", "size"), rev=("Value", "sum"),
                                                fee=("Delivery fee", "sum"),
                                                cost=("Shipping costs", "sum"))
    sb["net"] = sb.fee - sb.cost
    D["ship_bands"] = {"band": labels, "orders": sb.orders.astype(int).tolist(),
                       "fee": lst(sb.fee, 0), "cost": lst(sb.cost, 0), "net": lst(sb.net, 0)}
    wrong = eco[(eco.Value >= 55) & (eco["Delivery fee"] > 0)]
    D["wrong_fee"] = {"orders": int(len(wrong)), "eur": r(wrong["Delivery fee"].sum(), 0),
                      "min_value": r(wrong.Value.min(), 2), "max_value": r(wrong.Value.max(), 2)}
    # what the website actually does: free from 5 bags
    fee_by_qty = eco.groupby("Quantity")["Delivery fee"].apply(lambda s: (s > 0).mean() * 100)
    D["fee_share_by_qty"] = lst(fee_by_qty, 0)

    # ---------- regions ----------
    pv = eco.groupby("Ship to (province)").agg(orders=("kg", "size"), rev=("Value", "sum"))
    pv["pop_k"] = pv.index.map(POPULATION)
    pv["per_1000"] = pv.orders / pv.pop_k
    pv = pv.sort_values("per_1000")
    D["provinces"] = {"name": pv.index.tolist(), "orders": pv.orders.astype(int).tolist(),
                      "pop_k": pv.pop_k.astype(int).tolist(), "per_1000": lst(pv.per_1000, 1),
                      "rev": lst(pv.rev, 0)}
    bench = pv.drop(["Noord-Holland", "Zuid-Holland"]).orders.sum() / pv.drop(
        ["Noord-Holland", "Zuid-Holland"]).pop_k.sum()
    gap = sum(max(0, bench * pv.loc[p, "pop_k"] - pv.loc[p, "orders"]) for p in ["Noord-Holland", "Zuid-Holland"])

    # ---------- B2B ----------
    bc = b2b.groupby(["Customer", "City"]).agg(deliveries=("kg", "size"), kg=("kg", "sum"),
                                               rev=("Value", "sum")).reset_index()
    city = b2b.groupby("City").agg(clients=("Customer", "nunique"), kg=("kg", "sum"),
                                   rev=("Value", "sum")).sort_values("rev", ascending=False)
    D["b2b_city"] = {"city": city.index.tolist(), "clients": city.clients.astype(int).tolist(),
                     "kg": lst(city.kg, 0), "rev": lst(city.rev, 0)}

    # ---------- headline numbers ----------
    eco_rev, b2b_rev = eco.Value.sum(), b2b.Value.sum()
    ship_net = eco["Delivery fee"].sum() - eco["Shipping costs"].sum()
    out_total = rst.out_kg.sum()
    D["kpi"] = {
        "revenue": r(eco_rev + b2b_rev, 0), "eco_rev": r(eco_rev, 0), "b2b_rev": r(b2b_rev, 0),
        "eco_orders": int(len(eco)), "orders_per_day": r(len(eco) / 365, 0),
        "b2b_clients": int(b2b.Customer.nunique()), "b2b_deliveries": int(len(b2b)),
        "b2b_share": r(b2b_rev / (eco_rev + b2b_rev) * 100, 1),
        "sold_kg": r(demand.kg.sum(), 0), "roasted_kg": r(out_total, 0),
        "green_in_kg": r(rst.in_kg.sum(), 0),
        "scrap_kg": r(scrap_kg, 0), "scrap_eur": r(scrap_eur, 0),
        "scrap_share_of_output": r(scrap_kg / out_total * 100, 1),
        "scrap_days_of_orders": r(scrap_kg / (eco.kg.sum() / 365), 0),
        "scrap_green_cost": r(scrap_kg / (1 - rst.shrink.mean()) * avg_green_price, 0),
        "avg_green_price": r(avg_green_price, 2),
        "rejected_batches": int(rst.rejected.sum()), "rejected_kg": r(rst.rej_kg.sum(), 0),
        "ontime": r((1 - eco.late.mean()) * 100, 1), "late_orders": int(eco.late.sum()),
        "avg_lead_days": r(eco.lead.mean(), 2),
        "ship_net": r(ship_net, 0), "ship_net_pct": r(ship_net / eco_rev * 100, 1),
        "ship_cost_per_kg_eco": r(eco["Shipping costs"].sum() / eco.kg.sum(), 2),
        "ship_cost_per_kg_b2b": r(b2b["Shipping costs"].sum() / b2b.kg.sum(), 2),
        "fg_avg_value": r(fv.sum(axis=1).mean(), 0),
        "fg_peak_cover_days": r(cover.max().max(), 0),
        "green_min_cover_days": r((gs.sum(axis=1) / avg_use.sum() * 30.4).min(), 0),
        "randstad_gap_orders": r(gap, 0), "randstad_gap_pct": r(gap / len(eco) * 100, 0),
        "bench_per_1000": r(bench, 1),
        "peak_ratio": r(dem.sum(axis=1).max() / dem.sum(axis=1).min(), 2),
        "q4_vs_mid": r(dem.sum(axis=1).loc[9:12].mean() / dem.sum(axis=1).loc[3:8].mean(), 2),
        "shrink": r(rst.shrink.mean() * 100, 1),
    }

    # ---------- model inputs for the growth simulator ----------
    D["sim"] = {
        "base_demand": lst(dem.sum(axis=1), 0),
        "b2b_month": lst(b2b_kg, 0),
        "base_capacity": lst(prod.sum(axis=1), 0),  # current output = 1 shift
        "workdays": D["workdays"],
        "shrink": r(rst.shrink.mean(), 3),
        "container_kg": CONTAINER_KG,
        "price_per_kg": r((eco_rev + b2b_rev) / demand.kg.sum(), 2),
        "ship_net_per_order": r(ship_net / len(eco), 2),
        "kg_per_order": r(eco.kg.sum() / len(eco), 2),
        "setup_share": r((rst.batches * rst["Setup time p/batch"]).sum() / (rst.batches * rst.cycle).sum(), 3),
        "reject_rate": r(rst.rejected.sum() / rst.batches.sum(), 4),
        "light_reject_rate": r(by_roast.loc["Light", "rate"] / 100, 4),
        "light_share": r(prod["Light"].sum() / prod.sum().sum(), 3),
    }

    # ---------- write ----------
    tpl = (HERE / "deck_template.html").read_text(encoding="utf-8")
    data_js = "const D = " + json.dumps(D, ensure_ascii=False) + ";"
    page = tpl.replace("/*__DATA__*/", data_js)
    cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/plotly.js/2.34.0/plotly.min.js"></script>'
    (OUT / "Bean_There_Pitch.html").write_text(page.replace("<!--__PLOTLY__-->", cdn), encoding="utf-8")
    local = HERE / "plotly.min.js"
    if local.exists():
        inline = "<script>" + local.read_text(encoding="utf-8") + "</script>"
        (OUT / "Bean_There_Pitch_offline.html").write_text(
            page.replace("<!--__PLOTLY__-->", inline), encoding="utf-8")
    (HERE / "kpis.json").write_text(json.dumps(D["kpi"], indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(D["kpi"], indent=2, ensure_ascii=False))
    print(json.dumps(D["machines"], indent=2))
    print(json.dumps(D["quality"], indent=2))


if __name__ == "__main__":
    main()
