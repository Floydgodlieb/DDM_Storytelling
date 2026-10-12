"""
Bean there done that - Storytelling with Data
CRISP-DM analysis + presentation visuals (Python / pandas / matplotlib)

Run:  python bean_there_analysis.py "Bean_there_done_that_data_1.xlsx"
Output: KPI printout in the console + PNG charts in ./charts

CRISP-DM structure
  1. Business understanding  -> the question: is the company ready to grow next year?
  2. Data understanding      -> load 5 sheets, check consistency (stock reconciliations)
  3. Data preparation        -> clean column names, derive kg, months, lead times
  4. Modelling / analysis    -> KPIs per operation + growth scenario (+20% demand)
  5. Evaluation              -> charts with take-away titles (on the slides)
  6. Deployment              -> advice to the CEO (on the slides)
"""
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA = sys.argv[1] if len(sys.argv) > 1 else "Bean_there_done_that_data_1.xlsx"
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "charts"); OUT.mkdir(exist_ok=True)

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
MLAB = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MNUM = {m: i + 1 for i, m in enumerate(MONTHS)}

# ---------------------------------------------------------------- style (SWD: grey + one accent)
BG = "#F7F3EC"; INK = "#2B1D16"; MUTED = "#6B625B"; GREY = "#B9B2A9"; LIGHT = "#DDD6CC"
ACCENT = "#C4561B"   # problems / focus
BLUE = "#2F6DB5"     # demand / opportunity
plt.rcParams.update({
    "font.family": "Inter", "font.size": 19, "text.color": INK,
    "axes.edgecolor": GREY, "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.spines.top": False, "axes.spines.right": False, "axes.facecolor": BG,
    "figure.facecolor": BG, "savefig.facecolor": BG, "axes.grid": False,
})

def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=100)
    plt.close(fig)

def k(x):  # thousands formatter
    return f"{x/1000:,.0f}k"

# ================================================================ 2-3. DATA UNDERSTANDING & PREPARATION
x = pd.read_excel(DATA, sheet_name=None)
raw = x["Inventory (raw material)"].copy()
raw.columns = ["product", "supplier", "month", "stock", "unit", "scrap", "reason", "price", "stock_value", "purchased"]
fin = x["Inventory (finished product)"].copy()
fin.columns = ["product", "month", "stock", "unit", "scrap", "reason", "price", "stock_value"]
ro = x["Roasting"].iloc[:, :15].copy()
ro.columns = ["machine", "month", "product", "workdays", "batches_day", "load_kg", "final_kg", "setup_min",
              "run_min", "cool_min", "pack_min", "qc_weight", "qc_color", "qc_profile", "rejected"]
ec = x["E-com sales orders by product"].iloc[:, :9].copy()
ec.columns = ["product", "bag", "qty", "value", "order_date", "delivery_date", "fee", "ship_cost", "province"]
b2b = x["B2B orders"].copy()
b2b.columns = ["customer", "city", "product", "bag", "qty", "value", "delivery_date", "ship_cost"]

for d in (raw, fin, ro):
    d["m"] = d["month"].map(MNUM)
fin["product"] = fin["product"].str.title()
ro["product"] = ro["product"].str.title()
ec["kg_per_bag"] = np.where(ec.bag == 1, 1.0, 0.5)          # bag type 1 = 1 kg, 2 = 0.5 kg (price check)
ec["kg"] = ec.qty * ec.kg_per_bag
ec["m"] = ec.order_date.dt.month
b2b["kg"] = b2b.qty                                           # B2B = 1 kg bags only
b2b["m"] = b2b.delivery_date.dt.month

# roasting derived figures
ro["batches"] = ro.batches_day * ro.workdays
ro["good_batches"] = ro.batches - ro.rejected
ro["green_in_kg"] = ro.batches * ro.load_kg
ro["roasted_out_kg"] = ro.good_batches * ro.final_kg
ro["machine_h_day"] = ro.batches_day * (ro.setup_min + ro.run_min) / 60
ro["pack_h_day"] = ro.batches_day * ro.pack_min / 60

# monthly demand (kg) and production (kg) per product
demand = ec.pivot_table(index="m", columns="product", values="kg", aggfunc="sum")
demand["Medium Roast"] += b2b.groupby("m").kg.sum()
production = ro.pivot_table(index="m", columns="product", values="roasted_out_kg", aggfunc="sum")
fg_stock = fin.pivot_table(index="m", columns="product", values="stock")
fg_scrap = fin.pivot_table(index="m", columns="product", values="scrap")

# consistency check: stock(t) = stock(t-1) + production - demand + scrap  -> should be ~0
recon = fg_stock - (fg_stock.shift(1) + production - demand + fg_scrap)
print("Finished-goods reconciliation max abs diff (kg):", recon.abs().max().max())

# raw materials: implied consumption = previous stock + purchased + scrap - stock
rs = raw.pivot_table(index="m", columns="product", values="stock")
rp = raw.pivot_table(index="m", columns="product", values="purchased")
rsc = raw.pivot_table(index="m", columns="product", values="scrap")
consumption = rs.shift(1) + rp + rsc - rs
beans = [c for c in rs.columns if "Beans" in c]
print("Bean consumption vs roaster input (should match):")
print(pd.DataFrame({"inventory": consumption[beans].sum(axis=1), "roaster": ro.groupby("m").green_in_kg.sum()}).round(0))

# packaging check -> DATA QUALITY ISSUE: bag stock does not match bags sold
bags_sold_05 = ec[ec.bag == 2].groupby("m").qty.sum()
print("0.5 kg bags sold per month vs bags used according to inventory:")
print(pd.DataFrame({"sold": bags_sold_05, "inventory_use": consumption["Coffee bag w/valve 0,5"]}))

# ================================================================ 4. KPIs
K = {}
K["revenue_ecom"] = ec.value.sum(); K["revenue_b2b"] = b2b.value.sum()
K["kg_sold"] = demand.sum().sum(); K["kg_roasted"] = production.sum().sum()
K["orders_per_day"] = ec.groupby("order_date").size().mean()
K["aov"] = ec.value.mean()
K["fg_scrap_kg"] = -fin.scrap.sum(); K["fg_scrap_value_sales"] = -(fin.scrap * fin.price).sum()
K["scrap_pct_output"] = K["fg_scrap_kg"] / K["kg_roasted"]
green_price = (raw[raw["product"].isin(beans)].assign(v=lambda d: d.purchased * d.price).v.sum()
               / raw[raw["product"].isin(beans)].purchased.sum())
K["green_price_kg"] = green_price
K["material_cost_roasted_kg"] = green_price * ro.green_in_kg.sum() / ro.roasted_out_kg.sum()
K["fg_scrap_material_cost"] = K["fg_scrap_kg"] * K["material_cost_roasted_kg"]
K["reject_rate"] = ro.rejected.sum() / ro.batches.sum()
K["yield"] = ro.roasted_out_kg.sum() / ro.green_in_kg.sum()
for mach, g in ro.groupby("machine"):
    K[f"{mach} h/day"] = g.groupby("m").machine_h_day.sum().mean()
    K[f"{mach} kg/h effective"] = (g.load_kg / ((g.setup_min + g.run_min) / 60)).mean()
K["packing h/day"] = ro.groupby("m").pack_h_day.sum().mean()

# delivery: promise = next working day (no weekends / NL holidays 2023)
hol = pd.to_datetime(["2023-01-01", "2023-04-07", "2023-04-09", "2023-04-10", "2023-04-27", "2023-05-05",
                      "2023-05-18", "2023-05-28", "2023-05-29", "2023-12-25", "2023-12-26", "2024-01-01"])
bday = pd.offsets.CustomBusinessDay(holidays=hol)
promise = pd.Series(pd.DatetimeIndex(ec.order_date.unique()) + bday, index=ec.order_date.unique())
ec["promised"] = ec.order_date.map(promise)
ec["days_late"] = (ec.delivery_date - ec.promised).dt.days.clip(lower=0)
K["on_time"] = (ec.days_late == 0).mean()
ec["wrong_fee"] = (ec.value > 55) & (ec.fee > 0)                # free shipping promised above EUR 55
K["wrong_fee_orders"] = ec.wrong_fee.sum(); K["wrong_fee_eur"] = ec.loc[ec.wrong_fee, "fee"].sum()
K["net_shipping_cost"] = ec.ship_cost.sum() - ec.fee.sum()
K["net_shipping_pct_rev"] = K["net_shipping_cost"] / K["revenue_ecom"]
for kk, v in K.items():
    print(f"{kk:32s} {v:,.3f}")

print("\nFee charged by bag type x quantity (rule actually applied = 'free from 5 bags'):")
print(pd.crosstab([ec.bag, ec.qty], ec.fee > 0))

# ================================================================ 5. VISUALS (one message per chart)

# C1 - customers frozen, basket size seasonal (two small panels, no dual axis)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(16.6, 5.6))
opd = ec.groupby("m").apply(lambda d: len(d) / d.order_date.nunique())
kpo = ec.groupby("m").kg.mean()
a1.plot(range(1, 13), opd, color=GREY, lw=3); a1.set_ylim(0, 800)
a1.text(12.2, opd.iloc[-1], f"{opd.mean():.0f}", va="center", color=INK, fontsize=22, weight="bold")
a1.set_title("Orders per day", loc="left", color=INK, fontsize=21, pad=14)
colors = [BLUE if m in (1, 2, 9, 10, 11, 12) else GREY for m in range(1, 13)]
a2.bar(range(1, 13), kpo, color=colors, width=0.7)
a2.set_title("Kg per order", loc="left", color=INK, fontsize=21, pad=14)
for m in (2, 6):
    a2.text(m, kpo[m] + 0.1, f"{kpo[m]:.1f}", ha="center", color=INK, fontsize=18)
for a in (a1, a2):
    a.set_xticks(range(1, 13), MLAB, fontsize=16)
a2.set_yticks([]); a2.spines["left"].set_visible(False)
fig.tight_layout(); save(fig, "c1_orders")

# C2 - flat production vs seasonal demand
fig, ax = plt.subplots(figsize=(16.6, 6.4))
d_tot = demand.sum(axis=1) / 1000; p_tot = production.sum(axis=1) / 1000
ax.fill_between(range(1, 13), p_tot, d_tot, where=p_tot > d_tot, color=ACCENT, alpha=0.18, interpolate=True)
ax.plot(range(1, 13), d_tot, color=BLUE, lw=3.5); ax.plot(range(1, 13), p_tot, color=ACCENT, lw=3.5)
ax.text(12.2, d_tot.iloc[-1], "Demand", color=BLUE, va="center", weight="bold")
ax.text(12.2, p_tot.iloc[-1], "Roasted", color=ACCENT, va="center", weight="bold")
ax.text(5.5, 57.5, "Overproduction\n→ goes into stock", color=ACCENT, ha="center", fontsize=18)
ax.set_xticks(range(1, 13), MLAB); ax.set_ylim(40, 80); ax.set_ylabel("tonnes per month")
ax.set_xlim(0.7, 13.3)
fig.tight_layout(); save(fig, "c2_prod_demand")

# C3 - finished-goods stock and expired coffee
fig, ax = plt.subplots(figsize=(16.6, 6.4))
st = fg_stock.sum(axis=1) / 1000; sc = -fg_scrap.sum(axis=1) / 1000
ax.bar(range(1, 13), st, color=LIGHT, width=0.7, label="Stock at month end")
ax.bar(range(1, 13), sc, bottom=st, color=ACCENT, width=0.7, label="Expired & scrapped")
for m in range(1, 13):
    if sc[m] > 0:
        ax.text(m, st[m] + sc[m] + 1, f"{sc[m]:.0f} t", ha="center", color=ACCENT, weight="bold")
ax.set_xticks(range(1, 13), MLAB); ax.set_ylabel("tonnes roasted coffee")
ax.legend(frameon=False, loc="upper left", fontsize=17)
fig.tight_layout(); save(fig, "c3_scrap")

# C4 - machine hours vs one shift
fig, ax = plt.subplots(figsize=(16.6, 5.0))
labels = ["Packing line", "Roaster Probat Px120", "Roaster Probat P60"]
vals = [K["packing h/day"], K["Probat Px120 h/day"], K["Probat P60 h/day"]]
ax.barh(labels, vals, color=[ACCENT if v >= 8 else GREY for v in vals], height=0.55)
ax.axvline(8, color=INK, lw=2, ls="--"); ax.text(8.05, 2.42, "8-hour shift", color=INK, fontsize=18)
for i, v in enumerate(vals):
    ax.text(v + 0.1, i, f"{v:.1f} h", va="center", weight="bold")
ax.set_xlim(0, 10); ax.set_xlabel("hours used per working day (setup + roasting / packing)")
fig.tight_layout(); save(fig, "c4_capacity")

# C5 - QC reject rate by roast
fig, ax = plt.subplots(figsize=(10, 5.0))
rr = (ro.groupby("product").rejected.sum() / ro.groupby("product").batches.sum() * 100).sort_values()
ax.barh(rr.index, rr.values, color=[ACCENT if v > 3 else GREY for v in rr.values], height=0.55)
for i, v in enumerate(rr.values):
    ax.text(v + 0.1, i, f"{v:.1f}%", va="center", weight="bold")
ax.set_xlim(0, 6.2); ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
ax.set_title("Batches rejected by quality control", loc="left", color=MUTED, fontsize=18)
fig.tight_layout(); save(fig, "c5_quality")

# C6 - green bean stock coverage
fig, ax = plt.subplots(figsize=(16.6, 6.0))
use_day = ro.groupby("m").green_in_kg.sum() / ro.groupby("m").workdays.first()
cover = rs[beans].sum(axis=1) / use_day
ax.axhspan(0, 15, color=ACCENT, alpha=0.10)
ax.text(0.85, 2.5, "Danger zone: < 3 weeks of beans", color=ACCENT, fontsize=17)
ax.plot(range(1, 13), cover, color=INK, lw=3, marker="o", ms=9)
for m in (7, 9, 11):
    ax.text(m, cover[m] - 4.2, f"{cover[m]:.0f} days", ha="center", color=ACCENT, weight="bold")
ax.set_xticks(range(1, 13), MLAB); ax.set_ylim(0, 40); ax.set_ylabel("working days of green beans in stock")
fig.tight_layout(); save(fig, "c6_beans")

# C7 - shipping fee & delivery reliability
fig, (a1, a2) = plt.subplots(1, 2, figsize=(16.6, 5.6), gridspec_kw={"width_ratios": [1.15, 1]})
over55 = ec[ec.value > 55]
vals = [(over55.fee == 0).sum(), over55.wrong_fee.sum()]
a1.barh(["Shipped free", "Charged €4.95 anyway"], vals, color=[GREY, ACCENT], height=0.55)
for i, v in enumerate(vals):
    a1.text(v + 2000, i, k(v), va="center", weight="bold")
a1.set_xlim(0, 150000); a1.set_xticks([]); a1.spines["bottom"].set_visible(False)
a1.set_title("Orders above €55 (free shipping promised)", loc="left", color=MUTED, fontsize=18)
dl = ec.days_late.value_counts().sort_index()
dl = pd.Series({"On time": dl.get(0, 0), "1 day late": dl.get(1, 0), "2+ days late": dl[dl.index >= 2].sum()})
a2.bar(dl.index, dl.values / len(ec) * 100, color=[GREY, ACCENT, ACCENT], width=0.6)
for i, v in enumerate(dl.values / len(ec) * 100):
    a2.text(i, v + 1.5, f"{v:.1f}%", ha="center", weight="bold")
a2.set_ylim(0, 105); a2.set_yticks([]); a2.spines["left"].set_visible(False)
a2.set_title("Parcels vs next-day promise", loc="left", color=MUTED, fontsize=18)
fig.tight_layout(); save(fig, "c7_delivery")

# C8 - orders per 1,000 inhabitants (population: CBS, 1 Jan 2023, rounded)
pop = {"Groningen": 596, "Friesland": 659, "Drenthe": 499, "Overijssel": 1175, "Flevoland": 444,
       "Gelderland": 2151, "Utrecht": 1388, "Noord-Holland": 2952, "Zuid-Holland": 3804,
       "Zeeland": 391, "Noord-Brabant": 2626, "Limburg": 1128}
pen = (ec.groupby("province").size() / pd.Series(pop)).sort_values()
fig, ax = plt.subplots(figsize=(16.6, 6.6))
ax.barh(pen.index, pen.values, color=[BLUE if p in ("Noord-Holland", "Zuid-Holland") else GREY for p in pen.index], height=0.65)
for i, v in enumerate(pen.values):
    ax.text(v + 0.3, i, f"{v:.0f}", va="center", fontsize=17)
ax.set_xticks([]); ax.spines["bottom"].set_visible(False); ax.tick_params(axis="y", labelsize=17)
ax.set_title("E-com orders per 1,000 inhabitants, 2023", loc="left", color=MUTED, fontsize=18)
fig.tight_layout(); save(fig, "c8_market")

# ================================================================ GROWTH SCENARIO (+20 % demand)
GROWTH = 0.20
cap_now = production.sum(axis=1).mean()                       # ~ one full shift (both roasters ~8 h/day)
p60_share = ro[ro.machine == "Probat P60"].roasted_out_kg.sum() / ro.roasted_out_kg.sum()
p60 = ro[ro.machine == "Probat P60"]; px = ro[ro.machine == "Probat Px120"]
f_p60 = 60 / p60.load_kg.mean()                                # fill batches to max size
f_px = (120 / px.load_kg.mean()) * ((px.setup_min.mean() + px.run_min.mean())
                                    / (p60.setup_min.mean() + px.run_min.mean()))  # + setup down to P60 level
uplift = p60_share * f_p60 + (1 - p60_share) * f_px
cap_quick = cap_now * uplift
d_next = demand.sum(axis=1) * (1 + GROWTH)
print(f"\nCapacity now {cap_now/1000:.1f} t/m, after quick wins {cap_quick/1000:.1f} t/m (+{uplift-1:.0%})")
print("Demand +20% per month (t):", (d_next / 1000).round(1).tolist())
print("Peak gap after quick wins (t/month):", ((d_next - cap_quick).clip(lower=0) / 1000).round(1).tolist())

fig, ax = plt.subplots(figsize=(16.6, 6.6))
ax.plot(range(1, 13), demand.sum(axis=1) / 1000, color=GREY, lw=2.5, ls=":")
ax.plot(range(1, 13), d_next / 1000, color=BLUE, lw=3.5)
ax.axhline(cap_now / 1000, color=ACCENT, lw=2.5)
ax.axhline(cap_quick / 1000, color=INK, lw=2.5, ls="--")
gap = (d_next - cap_quick).clip(lower=0) / 1000
ax.fill_between(range(1, 13), cap_quick / 1000, d_next / 1000, where=gap > 0, color=BLUE, alpha=0.15, interpolate=True)
ax.text(12.2, d_next.iloc[-1] / 1000, "Demand +20%", color=BLUE, va="center", weight="bold")
ax.text(12.2, demand.sum(axis=1).iloc[-1] / 1000 - 2.4, "Demand 2023", color=MUTED, va="center")
ax.text(12.2, cap_now / 1000 - 1.6, "Capacity today", color=ACCENT, va="center", weight="bold")
ax.text(12.2, cap_quick / 1000 + 2.0, "After quick wins", color=INK, va="center", weight="bold")
ax.text(1.5, 84, "Gap → 2nd shift\nin peak season", color=BLUE, fontsize=18)
ax.set_xticks(range(1, 13), MLAB); ax.set_ylim(40, 95); ax.set_xlim(0.7, 14.2); ax.set_ylabel("tonnes per month")
fig.tight_layout(); save(fig, "c9_growth")
print("Charts written to", OUT.resolve())
