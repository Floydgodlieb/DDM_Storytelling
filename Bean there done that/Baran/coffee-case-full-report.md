# Bean There Done That: from business understanding to CEO presentation

**The full story of the coffee case, as worked out by the consultancy team**
Prepared 9 October 2026. Every number comes from the case presentation or the 2023 dataset (`Bean there done that data.xlsx`) and was recomputed at least twice. The supporting files are in this folder (see Appendix D).

---

## How to read this document

The document follows CRISP-DM, the six-phase method the assignment asks for, and ends with the CEO presentation:

| Part | CRISP-DM phase | Question it answers |
|---|---|---|
| 1 | Summary | What is the answer, in one page? |
| 2 | Business understanding | What does the CEO need to decide, and what counts as "ready"? |
| 3 | Data understanding | What data is there, can it be trusted, and what does it show? |
| 4 | Data preparation | How was the data turned into something we can model? |
| 5 | Modelling | How much growth can the plant carry, and where does it break? |
| 6 | Evaluation | How sure are we, and which assumption matters most? |
| 7 | Deployment: the advice | What should the CEO do, in what order, and what is it worth? |
| 8 | The CEO presentation | How do we tell this so the CEO decides? Which graphs, and why? |
| 9 | Limits and open questions | What we do not know, and who must answer it |

**Labels.** Wherever a claim could be mistaken for certain, it carries a label:
- **[fact]**: measured in the 2023 data or stated in the case.
- **[model]**: calculated by our scenario model. It is a projection, not a measurement.
- **[assumption]**: something we had to assume because the data or case does not say it.
- **Provisional target**: a target we propose, subject to a feasibility check by the client. Never a promise.

---

## Part 1. Summary

**The CEO's question:** are we ready to grow as of next year? (case p. 5)

**Our answer:** not by reopening fully on 1 January. From spring, the plant can probably supply **about 10% more volume** than the 727.3 tonnes sold in 2023 [model, one year of data; roughly 6–12% depending on shelf life and plant rates], if three things hold:

1. **Production follows demand.** Today the company roasts the same amount every month while demand is seasonal. That built up spring stock, and 48 tonnes of coffee expired in summer.
2. **About 10.8 working hours a day in September to January** for both roasters and the packing line. Over the whole year this is about the same number of hours as in 2023, but moved into the busy months.
3. **The coffee keeps about 15 days.** That is the stock buffer the make-to-demand plan needs.

**Why:** the plant is full, and its three main resources (two roasters and one packing line) all run out at almost the same growth level. Fixing one machine only moves the bottleneck to the next one. What the company lacks is hours in the busy months, not a machine.

**What we recommend:** stay closed in the first quarter and fix the basics; then reopen from May at the earliest, capped and in phases, once a set of go/no-go checks ("gates") are green. Use business customers (B2B) as a first, contractable step. Growth beyond about 10% needs a second shift in September to January.

**What it is worth:**
- *Observed in 2023:* the expired coffee is worth €1,159,200 at selling price. That is not a cost and not a lost sale (there was no summer demand for it); the real loss is its production cost, which the data does not contain.
- *Projected, gross:* ending the expiry saves about €449k–724k a year in beans and bags. If an extra 10% of demand arrives at 2023 prices, revenue rises about €1.8M before costs, of which about €0.87M is left to pay for labour, energy and overhead.
- *Unknown:* labour and energy costs, so whether +10% is profitable cannot yet be judged.

**What the CEO must answer first:** how many hours can be staffed, how long the coffee keeps, the bean lead times, and how many parcels PostNL can carry on the busiest day.

---

## Part 2. Business understanding

### 2.1 The company (case pp. 4–11)

Bean There Done That is a small Dutch specialty coffee roaster: premium taste, premium price, Dutch market only, under 1% market share. It sells mostly online (e-commerce), plus some business customers (B2B). The case gives an annual output of about 1,000 tonnes.

The operation runs in seven stages (case p. 7):

| # | Stage | What happens |
|---|---|---|
| 1 | Sourcing | Green (unroasted) beans bought directly from farmers in Costa Rica, Uganda and Colombia, in 70 kg bags, 12 bags per pallet, 12 pallets per 20 ft container (10,080 kg per container); plus packaging |
| 2 | Raw-material storage | Beans and packaging in the warehouse |
| 3 | Roasting | Two roasters: Probat P60 (215 kg/h, batch 60) and Probat Px120 (480 kg/h, batch 120) |
| 4 | Cooling | After each roast |
| 5 | Packing | One fully automated packing line |
| 6 | Finished-goods storage | Packed coffee in the warehouse |
| 7 | Delivery | E-commerce via PostNL (next-day except weekends and holidays; free shipping above €55); B2B with the company's own truck |

Products: three roasts (Light, Medium, Dark), each in 500 g and 1 kg bags, six products in total.

### 2.2 The business problem

The company struggled to manage growth in earlier years. At the start of 2023 it stopped accepting new customers to reach a "steady state". The CEO now wants to know whether the company is ready to grow as of next year.

The case does not say why growth was hard before, and it does not say which calendar year "next year" is. Both stay open questions.

### 2.3 The decision behind the question

"Are we ready?" is a yes/no question, but the CEO's real decision is **whether and how to reopen customer intake**. We framed five options:

| Option | What it means |
|---|---|
| A. Stay closed, fix first | Fix planning, quality and policy, reopen later |
| B. Reopen capped | A limit on new volume per week or month |
| C. Reopen per channel | B2B first, or e-commerce first |
| D. Reopen time-phased | Open in the quiet months, throttle before the busy season |
| E. Reopen fully | Accept all new customers from 1 January |

**Main question:** to what extent, through which channel and under which conditions can the company accept extra demand next year without breaking its delivery promise, its quality and the freshness of its coffee, and which roadblocks must be removed first?

**Sub-questions, one per stage:**

| Stage | Sub-question | Hypothesis we tested |
|---|---|---|
| Demand | How large and seasonal is demand, per channel, roast, bag size and month? | Demand peaks in autumn while production is flat |
| Sourcing | How many days of bean and packaging stock are held? | Bean stock gets thin in busy months |
| Raw storage | How many pallets are needed at the peak? | Storage limits larger orders |
| Roasting | How much of the available time is used, and how much do setups and rejects take? | Roasting is the first bottleneck |
| Cooling | Does cooling block the roaster? | Cooling runs alongside the next roast and is not a separate limit |
| Packing | How many hours and bags per day does packing need? | Packing is a hidden bottleneck |
| Finished goods | How do stock days and expiry move against demand? | A flat plan overstocks in spring and runs thin in winter |
| Delivery | What share arrives on time, and does it drop when volume rises? | Next-day delivery suffers when volume rises |

### 2.4 What "ready" means: success criteria

**Business success criterion:** the company is "ready" for a given growth level when, in its busiest month, every stage has enough capacity *and* three guardrails hold: the delivery promise, product quality, and freshness (no expired coffee).

**Data-mining goals** (what the analysis had to produce):
1. A 2023 baseline with KPIs for every stage.
2. A demand profile by channel, roast, bag size and month.
3. A capacity model that shows the **break point** of each stage: the growth level at which it first runs out of capacity.
4. Diagnostics on rejects, expiry, delivery and the shipping-fee rule.

**Data-mining success criteria:** the weight balance closes (green beans in → roasted → sold + stock change + expired + rejects); every KPI is defined and computed for all 12 months; every capacity figure is either sourced or labelled as an assumption; scenario results are shown as sensitivities, not forecasts.

### 2.5 Situation assessment

- **Resources:** one Excel workbook with five sheets, covering 2023 only; the case presentation; Python for the analysis. No access to the real client.
- **Constraints:** each roast is tied to one roaster (Medium on the P60; Light and Dark on the Px120) [fact, data]. All B2B volume is Medium in 1 kg bags, so B2B growth lands entirely on the smaller roaster. Beans arrive in full containers from three distant origins.
- **Risks to the analysis:** confusing units (green vs roasted vs sold tonnes); only one year of data, and a year with closed intake; no data on shift length, costs or warehouse capacity.
- **Terminology** (defined so nobody misreads a number):

| Term | Meaning in this report |
|---|---|
| Green kg | Unroasted beans going into the roaster |
| Roasted kg | Coffee coming out of the roaster (green minus roast loss) |
| Good kg | Roasted kg from batches that passed quality control |
| Sold kg | Coffee actually shipped to customers |
| Workday | A production day (254 in 2023: Monday to Friday minus Dutch holidays) |
| Days of cover | How many days the stock on hand would last at the coming month's sales |
| Make-to-demand | Roasting each month roughly what the coming weeks will sell, plus a small buffer (here ~15 days) |
| Flat plan | Roasting about the same amount every month, as in 2023 |
| Break point | The growth % at which a stage first runs out of hours in its busiest month |
| On time | Delivered by the next working day after the order date |

### 2.6 How Baran's first business understanding was reviewed

Baran wrote the first business understanding. The team's review found it **factually correct and honest**: it refused to call the company ready or unready before the evidence, noted that "1,000 tonnes" says nothing about spare capacity, and pointed out that closing intake does not freeze demand (which the data later proved). It was not yet complete as a CRISP-DM phase 1. The main improvements, all now built into this part:

1. Replace the yes/no question with the CEO's decision and options (§2.3).
2. Use all seven stages and add the assignment's own question: which KPIs per stage, and how does the company perform on them (case pp. 3, 6, 12).
3. Add success criteria, data-mining goals and a situation assessment (§2.4, §2.5).
4. Replace "agree with management" (impossible in a fictional case) with questions plus working assumptions.
5. Turn closed "Can …?" questions into open sub-questions with hypotheses.
6. Define units: the case's "~1,000 tonnes" turned out to be green beans going in, not coffee sold.

---

## Part 3. Data understanding

### 3.1 What data we received

One workbook, five sheets, calendar year 2023:

| Sheet | One row is | Rows | What it contains |
|---|---|---|---|
| Inventory (raw material) | one material in one month | 72 | Month-end stock, purchases, scrap for the three bean origins, two bag sizes and shipping boxes |
| Inventory (finished product) | one roast in one month | 36 | Month-end stock in kg, scrap (expired), selling price |
| Roasting | one machine × roast × month | 36 | Workdays, batches per day, load and final weight, setup, run, cooling and packing minutes, rejected batches by reason |
| E-com sales orders | one order of one product | 240,352 | Product, bag type, quantity, value, order and delivery date, delivery fee, shipping cost, province |
| B2B orders | one delivery to one customer | 273 | Customer, city, product, quantity, value, delivery date, shipping cost |

**Coverage per stage:**

| Stage | Covered by | Not in the data |
|---|---|---|
| Sourcing | Purchases, stock, scrap per origin | Order dates, lead times, supplier reliability |
| Raw storage | Month-end stock | Warehouse capacity |
| Roasting | Batches, weights, minutes, rejects | Shift length, staffing, downtime |
| Cooling | Cooling minutes per batch | Whether cooling blocks the roaster |
| Packing | Packing minutes per batch | Line capacity in bags per hour |
| Finished goods | Month-end stock, expiry | Shelf life, warehouse capacity |
| Delivery | Order and delivery dates, fees, costs | PostNL capacity, B2B order dates, truck payload |
| Demand | Every order | Customer IDs, lost sales, years before 2023 |
| Not covered at all | — | People and hours, cost price, margins, the CEO's growth target |

### 3.2 Data quality: can we trust it?

**Yes, to the kilogram.** The sheets agree with each other every month:
- **Finished goods:** closing stock = opening + good production − sales − expired, within 1 kg per month.
- **Green beans:** closing stock = opening + purchases − beans roasted − scrap, within 2.5 kg per month.

**Issues found and how we handled them:**

| Issue | What we found | Handling |
|---|---|---|
| Duplicate rows | 119,101 e-commerce rows are exact duplicates. Four tests show they are real, separate orders that happen to look identical (the stock balance only closes with them; box use matches order count). | Kept |
| Packaging records | The bag stock implies 170,000 500 g bags used, but 908,857 were shipped (×5.35). No unit explains it. | Excluded from KPIs; question for the client |
| Shipping-fee rule | The case says free shipping above €55; the data charges the fee on 1–4 bags and drops it from 5 bags. | Reported as a finding |
| "~1,000 t output" | Matches green beans (987.8 t bought, 966.6 t roasted), not sales (727.3 t) | Always state which stage a tonnage refers to |
| Very regular data | Exactly 658 or 659 orders every day; flat €6.75 shipping cost | No trend extrapolation |
| Stock valued at selling price | The finished-goods "unit price" is the consumer price | Stock value is not read as cost |
| Missing units | Batch size has no unit (kg assumed); the month sheets have no year | Labelled as assumptions |
| Bag codes | Bag type 1 = 1 kg, 2 = 500 g, worked out from the prices | Labelled as evidence |

### 3.3 What the data shows: the 2023 baseline per stage

**Where the beans went in 2023 [fact]:**

| Step | Tonnes |
|---|---|
| Green beans bought | 987.8 (98 containers) |
| Green beans roasted | 966.6 |
| Roasted coffee | 795.7 (roast loss 17.7%: Dark 19.8%, Medium 16.8%, Light 14.1%) |
| Good coffee after rejected batches (17.0 t) | 778.7 |
| Sold | 727.3 (e-commerce 711.0 = 97.8%; B2B 16.3 = 2.2%) |
| Expired | 48.0 |
| Added to stock over the year | 3.5 |

So it takes about 1.33 kg of green beans to sell 1 kg of coffee.

**Demand [fact]**
- E-commerce sold 1,650 kg a day in March–August and 2,306 kg a day in September–December. February was the busiest month (2,318 kg a day); January was 1,973.
- The number of orders is flat (658–659 every day). What changes is the **size** of each order: 2.49 kg in March up to 3.52 kg in February. Customers order bigger bags in the busy months.
- Mix is stable: Dark 44.2%, Medium 36.3%, Light 19.5% of kg sold.
- B2B: 21 fixed customers, each delivered every four weeks (13 rounds a year), about 1,252 kg per round, Medium in 1 kg bags only. No new and no lost B2B customers, consistent with the intake stop.

**Sourcing and raw storage [fact]**
- Beans are bought in lots of two containers (20,160 kg).
- Days of stock per origin dropped very low: **Uganda 0.9 production days at the end of July**, Colombia 4.9 (July), Costa Rica 5.8 (September). This happened without any growth.
- 5,040 kg of green beans expired in May, after the April stock peak.
- Peak green stock: 136 pallets at month-end (April); up to 224 pallets within a month if a whole month's purchases arrive at once.

**Roasting [fact]**

| | P60 (Medium) | Px120 (Dark + Light) |
|---|---|---|
| Hours per workday (setup + roasting) | 8.02 (peak 8.36, May) | 8.53 (peak 9.07, July) |
| Green beans roasted per year | 333.8 t | 632.8 t |
| Real speed incl. setup vs nameplate | 164 kg/h = 76% of 215 | 292 kg/h = 61% of 480 |
| Share of time spent on setup | 20.4% | 27.2% |
| Batch fill (load ÷ max batch) | 91.4% | 91.7% |

- Rejected batches: Dark 1.55%, Medium 1.28%, **Light 4.96%** (up to 8.9% in February).

**Cooling [fact + assumption]:** 9.0 minutes per batch on the P60 and 10.7 on the Px120, about half a roast cycle. If cooling blocked the drum, 2023 would have needed 11.6–12.6 hours a day, which were clearly not worked, so we assume cooling runs alongside the next roast.

**Packing [fact]:** 8.30 hours per workday on average, up to 9.17 in August; 369 kg per hour on average, 412–415 kg per hour in the best months; about 5,162 bags per production day.

**Finished goods [fact]**
- Production was flat (58–71 t per month) while sales swung between 51 and 73 t.
- From March to August the company produced 83 t more than it sold. Stock climbed to 31–49 days of sales by May.
- **48 t expired in June–August** (Dark 30 t, Medium 12 t, Light 6 t), 6.2% of good production.
- From September to December sales exceeded production; stock fell to only 12–18 days of sales in December and January.

**Delivery [fact]**
- **92.07%** of e-commerce orders arrived by the next working day after the order date (the recommended definition). With weekends only as non-working days the figure is 88.05%; with "next calendar day" it is 63.84%. Which definition you use matters, so it must be stated.
- Every late parcel is exactly one working day late, and the late share is the same in every month and every province (about 8%). That points to a carrier hand-over pattern, not to overload.
- Mondays carry 1,848 parcels on average against 727 on Tuesday to Friday; the busiest day was 27 December with 3,070.

**Shipping economics [fact]**
- The €4.95 fee is charged on every order of 1–4 bags and never from 5 bags, whatever the value. **30,725 orders above €55 still paid the fee: €152,088.75.**
- PostNL cost €1,622,376 (€6.75 per parcel); fees collected €599,143; net shipping cost **€1,023,233 = 5.8% of e-commerce revenue** (€17.56M).

### 3.4 Answers to the business-understanding claims

| Claim | What the data says |
|---|---|
| "~1,000 t annual output" | True only as green beans; sold is 727.3 t |
| "Mostly e-commerce, some B2B" | True: 97.8% of volume is e-commerce |
| "No new customers since 2023" | True for B2B; not testable for e-commerce (no customer ID) |
| "Stopping intake does not guarantee stable demand" | Strongly confirmed: order size swings ±40% between seasons |
| "Free shipping above €55" | Not what happens in practice |
| "Next-day delivery" | 92.07% by the next working day |
| "Struggled to manage growth" before 2023 | Not testable: no data before 2023 |
| People, money, management capacity | No data |

---

## Part 4. Data preparation

- **Units:** bag type converted to kg (1 kg or 0.5 kg); roast names made consistent across sheets ("Dark roast" vs "Dark Roast").
- **Dates:** e-commerce counted by order date, B2B by delivery date (the only date it has), stock at month-end.
- **Calendar:** the non-working weekdays were read from the data itself (eight weekdays with zero deliveries: Good Friday, Easter Monday, King's Day, Ascension, Whit Monday, Christmas, Boxing Day, New Year's Day).
- **Monthly table:** one row per month with demand, production, stock, cover, expiry, machine hours and on-time delivery (`baseline_monthly.csv`).
- **Rates per roast:** green kg per good kg, roaster hours per green kg, cooling and packing hours, reject rate, batch fill; these feed the model.
- **Excluded:** the packaging stock records (they do not reconcile).

---

## Part 5. Modelling: how much growth can the plant carry?

### 5.1 The model in plain words

A transparent, month-by-month spreadsheet-style model, built in Python. It follows the chain backwards from customers to beans:

1. **Demand:** 2023 sales per month, roast and channel, scaled up for growth.
2. **Good coffee needed:** set by the production plan: either the 2023 flat plan, or make-to-demand with ~15 days of stock.
3. **Green beans needed:** good kg × the 2023 green-to-good ratio per roast (roast loss plus rejects).
4. **Roaster hours:** green kg × the 2023 hours per kg on each machine (Medium on the P60, Dark and Light on the Px120).
5. **Packing hours:** good kg × the 2023 packing hours per kg.
6. **Capacity test:** in each month, are the hours needed per workday within the hours available?

There is **no machine learning** in it. One year of data cannot separate a trend from a seasonal pattern, so a fitted forecast would be a guess dressed up as a result.

**Check:** with 2023 demand and the flat plan, the model reproduces 2023 exactly: machine hours within 0.01%, green, good, sold and expired tonnes within 0.02 t.

### 5.2 Scenarios

**Demand scenarios** (placeholders until the CEO states an ambition) [assumption]:
- S0: 2023 repeated · S1: +10% · S2: +25% · S3: +25%, all of it in September–December.

**Hours available per workday** (the real shift pattern is not in the data) [assumption]:
- K1: 9.17 hours, the highest monthly average actually worked in 2023 · K2: 10 hours · K3: two shifts, 16 hours.

**Production plans:**
- Flat plan (2023 practice; expiry continues and grows with volume).
- Make-to-demand with ~15 days of stock (no expiry, but more hours needed in the busy months).

### 5.3 Results

**Hours needed per workday in the busiest month [model]:**

| Scenario | Flat plan (P60 / Px120 / packing) | Make-to-demand (P60 / Px120 / packing) |
|---|---|---|
| 2023 volume | 8.79 / 8.92 / 8.81 (April) | 9.77 / 9.79 / 9.72 (December) |
| +10% | 9.67 / 9.81 / 9.69 | 10.74 / 10.77 / 10.70 |
| +25% | 10.99 / 11.15 / 11.01 | 12.21 / 12.24 / 12.15 |
| +25% in Sep–Dec only | ~11 h, but 192 t of stock built up (101 days of cover) | 14.45 / 15.15 / 14.81 (September) |

**Break points: how much uniform growth fits before the busiest month runs out of hours [model]:**

| Resource | Today's peak hours (9.17), flat plan | 10 h, flat plan | 10 h, make-to-demand | Two shifts, flat plan | Two shifts, make-to-demand |
|---|---|---|---|---|---|
| Px120 | +2.8% | +12.1% | +2.2% | +79% | +63% |
| Packing line | +4.1% | +13.5% | +2.8% | +82% | +65% |
| P60 | +4.3% | +13.8% | +2.4% | +82% | +64% |

**The plant is balanced.** In every variant, all three resources break within about 1.5 percentage points of each other. There is no single bottleneck to fix.

**The headline scenario: more hours only in the busy months** (make-to-demand, 15 days of stock) [model]:

| Hours Sep–Jan / Feb–Aug | Maximum growth | First to break |
|---|---|---|
| 10.8 h / 8.5 h | +9.9% | P60 in April |
| 10.8 h / 9.17 h | +10.3% | Px120 in December |
| 10.0 h / 9.17 h | +2.2% | Px120 |
| 16 h / 9.17 h (two shifts in winter) | +18.6% | P60 |

**How many hours does +10% really take?** About the same total as 2023 (P60 +122 h, Px120 +18 h, packing +55 h per year), because make-to-demand removes the wasted spring production. But the hours move into September–January: about **180–230 hours per resource above an 8-hour day** (182–210 h in Sep–Jan, 198–229 h over the whole year), or 130–160 h above an 8.5-hour day.

### 5.4 Fix levers: do machine improvements solve it?

| Lever | Hours freed per year | Effect on the first break point (today's peak hours) |
|---|---|---|
| Px120 setup share from 27% to 20% (as on the P60) | 185 h on the Px120 | Px120 moves to +12.4%, but packing now breaks at +4.1% |
| Light rejects from 4.96% to 1.5% | 20 h; 6.5 t green beans | small |
| Batch fill to 95% | 78 h (P60), 74 h (Px120) | packing still breaks at +4.1% |
| All three together | ~350 roaster hours | **packing caps growth at +4.1%** (+13.5% at 10 h) |
| Packing at the speed of the best 2023 months (~412–415 kg/h) | — | roughly +14% at today's peak hours [hand calculation] |

**Lesson:** improving the roasters alone does not lift growth, because the packing line is right behind them. Growth needs extra hours on the whole line.

### 5.5 Other resources

| Resource | Finding [model] |
|---|---|
| Green-bean storage | Passes the 2023 peak of 224 pallets at about +35–40% growth; real capacity unknown |
| PostNL | Busiest day 3,070 parcels → about 3,377 at +10%, 3,838 at +25%; capacity unknown |
| B2B truck | Biggest round 1,325 kg → about 1,458 at +10%; payload unknown |
| B2B growth (option C) | Medium only, on the P60: about 11 t a year at today's hours, 36 t at 10 h (flat plan), 5 t at 10 h (make-to-demand) |

---

## Part 6. Evaluation: how sure are we?

### 6.1 Which assumption matters most

| Assumption | If it changes… | Effect |
|---|---|---|
| **Hours available** | 8 h → 9.17 h → 10 h → 16 h | Growth room moves from none, to +3–4%, to +12–14%, to +60–80%. **By far the largest effect.** |
| **Shelf life / stock buffer** | 7 / 10 / 15 / 20 / 30 days | +6.1% / +7.6% / +10.3% / +12.3% / +6.1%. Too little buffer means more peak hours; too much means stock built too early. |
| **Cooling blocks the roaster** | parallel vs blocking | Blocking would make even two shifts give only +10–25%. Unlikely: the hours worked in 2023 could not cover it. |
| **Plant rates per month instead of per year** | annual vs monthly 2023 rates | Growth room +8.3% instead of +10.3% |
| **New customers buy like 2023 customers** | price, mix, seasonality | Untested: intake was closed. If new customers are more seasonal, the peak gets worse. |

### 6.2 Confidence per conclusion

| Conclusion | Confidence | Why |
|---|---|---|
| No growth room at today's hours | High | Follows directly from 2023 hours |
| The plant is balanced (no single bottleneck) | High | Holds in every variant |
| The flat plan causes the summer expiry | Medium | Strong pattern, but an explanation, not a tested cause |
| About +10% with ~10.8 h in Sep–Jan | Medium | Depends on hours, shelf life and one year of data |
| Which resource breaks first | Low–medium | The three are within ~1.5 points; it changes with small assumptions |
| Euro values | Medium | Ranges given; costs unknown |

### 6.3 What the model cannot say

It shows what the plant can **produce**, not what customers will **buy**. It cannot forecast demand, cannot value labour or energy, and cannot confirm warehouse, PostNL or truck capacity.

---

## Part 7. Deployment: the advice

### 7.1 The recommendation

**Do not reopen fully on 1 January.** Use the first quarter to fix the basics, then reopen from May at the earliest, **capped and phased**, to about +10% [model], once the gates below are green. Start with B2B as a contractable first step. Above about 10%, decide on a second shift in September–January.

### 7.2 The options compared

| Option | Growth possible [model] | Main risk | Verdict |
|---|---|---|---|
| A. Stay closed, fix first | 0% new intake | Commercial cost of another closed year (unknown) | **Right for Q1 as the fix window**, wrong as a full-year stance |
| B. Reopen capped | ~+10% with 10.8 h in Sep–Jan; +2–3% at 10 h all year | Cap must follow confirmed hours | **Recommended** as the control |
| C. Reopen per channel | B2B ~5–36 t a year (Medium, P60 only); e-com ~15–86 t | Truck payload, PostNL capacity | **B2B as first step**, not the growth engine |
| D. Reopen time-phased | Same end volume as B, starting later | Needs a cap on Sep–Feb volume too | **Recommended** with B |
| E. Reopen fully on 1 January | Any growth breaks the busiest month | +25% = 3,838 parcels on the peak day; 60 t expired on the flat plan | **Reject** |

### 7.3 Roadblocks and improvements per stage

All targets are provisional, subject to a feasibility check.

| Stage | Evidence | Fix | KPI and provisional target |
|---|---|---|---|
| Sourcing | Uganda 0.9 days of stock (July); 5 t green expired; packaging records do not reconcile | Stock rule per origin; buy against the production plan; physical packaging count | ≥ 10 production days per origin; green expiry 0; packaging reconciles ±2% |
| Raw storage | Peak 136 pallets (224 within a month) | Confirm capacity; stagger container arrivals | Peak pallets ≤ 85% of capacity |
| Roasting | Setup 27% on Px120; batches 91% full; Light rejects 4.96% | Group Light and Dark runs to cut setups; root cause of Light rejects; fill to 95% | Setup ≤ 22%; Light rejects ≤ 2%; fill ≥ 95% |
| Cooling | ~half a roast cycle | Confirm it runs in parallel | Confirmed yes/no |
| Packing | 8.30 h/day, 9.17 h peak; 369 kg/h | Find why speed varies; maintenance | ≥ 410 kg/h |
| Finished goods | 48 t expired; 31–49 days of stock in May | **Make-to-demand live before March** (the 2023 surplus started in March) | Expired 0 kg; 10–25 days of stock |
| Delivery | 92.07% on time; every late parcel 1 day late; Monday peaks | Review with PostNL; written peak capacity | ≥ 95% target, ≥ 92% guardrail |
| Commercial | Fee on 1–4 bags, not "free above €55" (€152k charged); net shipping 5.8% of revenue | CEO decides the rule; volume cap in kg per week | 0 orders charged against the published rule |

**On the shipping fee:** first confirm which rule customers actually see. If the website promises "free above €55", the company should ask its legal counsel about past orders before deciding. This report gives no legal advice.

### 7.4 Roadmap

| Phase | Actions |
|---|---|
| **Fix** (now to end Q1) | Confirm the open facts with the CEO; make-to-demand planning live before March; bean stock rule; shipping-fee decision; packaging count; root cause of Light rejects; PostNL review |
| **Prepare** (Q1–Q2) | Staff the Sep–Jan hours, hired and trained by August; setup and batch-fill programme; packing speed programme; monthly planning meeting; cap mechanism; B2B prospect list and truck check |
| **Reopen controlled** (from May, when the gates are green) | New B2B customers plus capped e-commerce intake, up to about +10%; monthly gate review; intake stops when a gate turns red; raise the cap only after the first busy season held |

### 7.5 Go/no-go gates (conditions, not promises)

| Gate | Condition | Owner |
|---|---|---|
| G1 Hours | Written staffing plan: ~10.8 h per workday in Sep–Jan and ≥ 8.5 h in Feb–Aug for both roasters and the packing line | Production manager with CEO/HR |
| G2 Planning | Make-to-demand has run 2 full months; 10–25 days of stock; 0 kg expired | Production planner |
| G3 Beans | Lead times confirmed; ≥ 10 production days of stock per origin for 3 months | Purchasing |
| G4 Delivery | On time ≥ 92% for 3 months; PostNL confirms ≥ 3,377 parcels on the peak day in writing | Logistics |
| G5 Quality | Light rejects ≤ 3% for 3 months | Roast master |
| G6 Promise | Shipping-fee rule decided and applied | CEO |
| G7 Data | Packaging stock reconciles within ±2% at a physical count | Finance / warehouse |
| G8 (above ~10%) | Cooling confirmed in parallel; warehouse and truck capacity confirmed | Production / logistics |

**Reviews:** September next year for the expiry results; February, after the first busy season, for the decision to raise the cap.

**Risks of the advice:** staffing ~10.8 h a day for five months (recruitment lead time, overtime limits, fatigue; owner CEO/HR); quality under longer days (watch Light rejects; owner roast master).

### 7.6 The value case (types never mixed)

| Item | Type | Figure |
|---|---|---|
| Expired finished coffee, 48 t | Observed 2023 | €1,159,200 at selling price: not a cost and not a lost sale; the real loss is its production cost (unknown) |
| Expired green beans, 5,040 kg | Observed 2023 | €40,236 at purchase price (a real cost) |
| Shipping fee charged against the published rule | Observed 2023 | 30,725 orders, €152,088.75; applying the rule would cost up to ~€152k revenue a year (projected) |
| Net shipping cost | Observed 2023 | €1,023,233 = 5.8% of e-commerce revenue |
| Inputs saved once expiry ends | Projected, gross | €449k–724k a year (range = cheapest vs dearest bean origin; point estimate ~€532k); the extra winter hours are not costed |
| Revenue from +10% | Projected, gross, before cost | ~€1.8M, *if* the extra demand arrives at 2023 prices and mix (€179,829 per +1%) |
| Known inputs for that growth | Projected | ~€12.72 per kg sold (beans, bags, net shipping, boxes) ≈ €92.5k per +1%, leaving ~€87k per +1% (~€0.87M at +10%) for labour, energy and overhead |
| Causally supported | — | None yet: nothing has been implemented |

**Cannot be valued yet:** labour cost per hour and shift premiums, cost price per roast, energy, stock-holding cost, the cost of the programmes, PostNL terms, and the cost of staying closed another year.

---

## Part 8. The CEO presentation

### 8.1 The Big Idea

> We are not ready to reopen on 1 January. From spring, the plant can probably supply about 10% more than in 2023 [model], if production follows demand, about 10.8 hours a day can be staffed in September to January, and the coffee keeps about 15 days. Reopening fully now would break the winter peak and coffee would keep expiring.

### 8.2 The story in three minutes

- **Situation:** intake has been closed since the start of 2023. That steady year shows where growth would break.
- **Complication:** customers order bigger bags in autumn and winter, not more orders. Production stays flat, so spring stock piled up and 48 tonnes expired in summer, while December ran short. Both roasters and the packing line already use a full working day, and all three run out at almost the same point.
- **Question:** can we grow next year, and how?
- **Answer:** probably about 10% from spring, capped and phased, once we roast to demand and staff longer days in September to January. We are short of hours in the busy months, not of a machine.
- **Ask:** four answers decide whether we can start in May: the hours you can staff, how long the coffee keeps, the bean lead times, and PostNL's peak-day capacity.

### 8.3 The storyline (pyramid)

**Governing thought:** not ready on 1 January; about +10% from spring, capped and phased, under three conditions.

1. **The plant is full in the months that matter:** 8.02 / 8.53 / 8.30 hours per workday; all three resources break within ~1.5 points of growth; roaster fixes alone free ~350 hours but packing then stops growth at +4.1%.
2. **The flat plan wastes the capacity we have:** 1,650 vs 2,306 kg a day; 31–49 days of stock in spring; 48 t expired; 12–18 days in December–January.
3. **Ending the waste and growing both need winter hours:** make-to-demand needs 9.8 hours a day in December even at 0% growth; +10% needs ~10.8 hours.

### 8.4 Slide by slide (13 slides + appendix)

Every title states the takeaway, not just the topic.

| # | Action title | Content | Visual |
|---|---|---|---|
| 1 | We are not ready to reopen on 1 January; from spring we can probably supply about 10% more, under three conditions | The answer, the three conditions, "model estimate on one year of data, roughly 6–12%, not a promise" | Text |
| 2 | A year with closed intake shows where growth would break first | The seven stages; 2023 is the only year of data | Process strip |
| 3 | Autumn and winter sell up to 2,318 kg a day against 1,650 in spring, but production stays flat | Orders flat; order size makes the season | Graph A |
| 4 | The flat plan piled up spring stock, and 48 tonnes expired in summer | 31–49 days in spring; 6.2% of production; 12–18 days in December | Graph B |
| 5 | Both roasters and the packing line already use a full working day | 8.02 / 8.53 / 8.30 h; shift length to confirm | Graph C |
| 6 | Fixing one machine is not enough: all three run out at almost the same growth level | ~1.5 points apart; ~350 h freed; packing caps +4.1% | Simple diagram |
| 7 | Producing to demand should end the expiry, but needs 9.8 hours a day in December even without growth | Plain definition of make-to-demand | Graph D (key chart) |
| 8 | If we can staff about 10.8 hours a day in September to January, about 10% more volume can be produced | Hours moved, not added; shelf-life table (7 d ~6.1%, 10 d ~7.6%, 15 d ~10.3%, 20 d ~12.3%); second shift for more | Graph E + table |
| 9 | A full reopening on 1 January breaks the peak month; a capped, phased reopening does not | Options A–E with verdicts | Options table |
| 10 | If an extra 10% of demand arrives at 2023 prices, revenue rises about €1.8M before costs [projected] | Observed / projected / unknown; cost of staying closed not valued | Three-column table |
| 11 | Five problems need fixing this winter, whether or not we grow | Uganda stock; Light rejects; shipping fee; late parcels; packaging records | Table |
| 12 | Fix by March, prepare by summer, reopen from May only when the gates are met | Roadmap, gates with owners, reviews | Timeline + checklist |
| 13 | Your answers on hours, shelf life, beans and PostNL decide whether we can start in May | The CEO's questions | Text |
| Appendix | Roadblocks per stage; option C detail; value case; data limits | | |

### 8.5 Why these graphs (none were made yet)

| Graph | The CEO question it answers | Why this form | How not to mislead |
|---|---|---|---|
| **A. Sales vs production per month** (line chart) | "Is my problem demand or production?" | A change-over-time chart shows the shape of the year: the surplus in spring and the shortfall in the busy months | One unit (tonnes), y-axis from zero, labelled "2023, observed" |
| **B. Days of stock per roast, with expired tonnes in a panel below** | "Where did the waste come from?" | Shows the order of events: stock piles up first, expiry follows | Two stacked panels instead of a second y-axis; a shaded 10–25-day band labelled "provisional target"; no shelf-life line, because shelf life is unknown |
| **C. Hours per workday per machine** (horizontal bars) | "How full are we?" | Bars compare sizes at a glance | Start at zero; a cut-off axis would make one machine look twice as busy; mark the 8-hour shift as "assumed, to confirm" |
| **D. Hours needed per month: flat plan vs make-to-demand, 2023 volume** (two lines) | "What does ending the waste cost me in hours?" | **The key chart.** It shows the work moving out of spring and into December (9.8 h a day) | Both lines labelled "model, 2023 demand"; available hours as a dashed line "to confirm" |
| **E. Hours needed per month at +10%** (bars) | "How many hours buy how much growth?" | Makes the winter peak (up to 10.77 h in December) visible against today's hours | Bars marked as estimates (lighter or hatched); annotated "about the same hours per year as 2023, moved into Sep–Jan" |

**Graphs not to show, and why:**
- A big "€1.16M lost" bar: it is selling price, not a cost, and it would be heard as money lost.
- A waterfall adding observed, projected and growth euros into one "prize": it mixes types of value.
- A demand trend or forecast line: one year of data has no trend.
- On-time delivery per month on a zoomed axis: it is flat at about 92%; zooming would turn noise into a story.
- A ranking that names one bottleneck: the plant is balanced, and the chart would suggest one machine fix.
- A 30-KPI traffic-light dashboard, a roast-mix pie or a supply-chain Sankey: decoration, no decision follows from them.

### 8.6 The three hardest CEO questions

**1. "Demand is there. Why not reopen on 1 January?"**
At today's hours any growth breaks the busiest months. At +25%, PostNL would need 3,838 parcels on the peak day and 60 tonnes would expire on the current plan. We start in spring, with a cap, once the winter hours are in place.

**2. "Can't we just buy another machine or speed up packing?"**
All three resources run out within about 1.5 points of growth of each other. Fixing the roasters frees about 350 hours a year, and then packing stops us at +4.1%. We are short of hours in September to January. Above about 10% you need a second shift or much longer days in those months (up to about +19%); beyond that, more hours in spring and summer too.

**3. "Can you guarantee 10%? What is it worth?"**
No. The model says about 10% more supply, roughly 6–12% depending on shelf life and plant rates, on one year of data. It holds only with ~10.8 hours in September to January, ~15 days of shelf life, PostNL carrying ~3,400 parcels on the peak day, and new customers who buy like today's. If that demand arrives at 2023 prices, revenue rises about €1.8M before costs [projected]. We need hardly more hours per year, but at a different time: about 180–230 hours per resource above an 8-hour day, which you can price at your own overtime or shift rate. We raise the cap only after the first busy season has held.

### 8.7 What must always be said out loud

- **Projections, never stated as fact:** ~+10% (roughly 6–12%), 10.8 h, 9.8 h, the hour figures, +4.1% and +13.5%, €449k–724k, ~€1.8M, ~€0.87M, all targets and gates.
- **Measured facts:** hours per workday, sales per day, 48 t expired, 92.07% on time, €152,088.75 in fees, €1,023,233 net shipping.
- **Always with €1,159,200:** "at selling price, not a cost and not a lost sale".
- **Assumptions that carry the advice:** staffable hours, cooling in parallel, ~15 days of shelf life, PostNL peak capacity, new customers buying like 2023 customers, and one closed-intake year standing in for next year.
- **Causally supported results:** none yet.

---

## Part 9. Limits and open questions

### 9.1 Data limits

- One year of data (2023), and a year with closed intake: no trend and no forecasting model.
- No customer IDs: retention, cohorts and new versus existing customers cannot be measured.
- No data on shift length, costs, shelf life, warehouse capacity, PostNL capacity or truck payload.
- Packaging stock records do not reconcile and were excluded.
- The data is unusually regular (exactly 658–659 orders a day), which suggests a constructed teaching dataset.

### 9.2 Questions for the CEO (1–4 are needed before the go decision)

1. How many hours per workday can each roaster and the packing line be staffed, per month, at what cost and with what lead time?
2. How long does each roast keep, and how is expiry decided? (In 2023 write-offs came in round lots of 5,000–6,000 kg.)
3. What lead time and minimum order does each bean origin need?
4. What peak-day capacity does the PostNL contract give, and why do 8% of parcels arrive exactly one day late?
5. Does cooling run alongside the next roast, or does it block the roaster?
6. What is the cost price per kg per roast, and the labour cost per hour?
7. How much growth do you want, and by when?
8. What are the truck payload and warehouse capacity, and what does a physical packaging count show?

---

## Appendix A. Glossary

| Term | Plain meaning |
|---|---|
| CRISP-DM | A six-phase method for data projects: business understanding, data understanding, data preparation, modelling, evaluation, deployment |
| KPI | Key performance indicator: a number that shows how well a part of the business performs |
| Break point | The growth level at which a resource first runs out of hours |
| Balanced plant | All main resources reach their limit at about the same time, so fixing one alone does not help |
| Make-to-demand | Producing roughly what will sell in the coming weeks instead of a flat amount |
| Days of cover | How long the stock on hand would last at expected sales |
| Projected vs observed | Projected = calculated for the future by a model; observed = measured in the data |
| Gate | A condition that must be met before the next step, checked monthly |

## Appendix B. KPI scorecard (2023)

| Stage | KPI | 2023 value | Status |
|---|---|---|---|
| Demand | E-commerce kg per day | 1,948 (Mar 1,641 – Feb 2,318) | info |
| Demand | Kg per order | 2.96 (2.49 – 3.52) | info |
| Sourcing | Lowest days of bean stock | Uganda 0.9 (July) | red |
| Sourcing | Green-bean expiry | 5,040 kg (0.51%) | amber |
| Raw storage | Peak pallets | 136 month-end, 224 within a month | capacity unknown |
| Roasting | Hours per workday | P60 8.02, Px120 8.53 | red against an assumed 8 h shift |
| Roasting | Real speed vs nameplate | P60 76%, Px120 61% | amber |
| Roasting | Light-roast rejects | 4.96% | red |
| Cooling | Minutes per batch | 9.0 / 10.7 | green if parallel |
| Packing | Hours per workday | 8.30 (peak 9.17) | red against an assumed 8 h shift |
| Finished goods | Expired coffee | 48 t = 6.2% of good production | red |
| Finished goods | Days of stock | Dark 30.0, Medium 23.5, Light 21.6 (peaks 31–49 in May) | red |
| Delivery | On time (next working day) | 92.07% | amber |
| Shipping | Fee charged above €55 | 30,725 orders, €152,088.75 | red |
| Shipping | Net shipping cost | €1,023,233 = 5.8% of e-com revenue | info |
| B2B | Customers, rounds | 21 customers, 13 rounds, 16.3 t | info |

Statuses use guardrails the team set as assumptions (for example, an 8-hour shift and 95% on time); the client has not confirmed them.

## Appendix C. How the team worked

| Step | Specialist | What it produced |
|---|---|---|
| 1 | Strategy consultant | Review of the business understanding; decision frame, options, KPI tree |
| 2 | Data analyst | Data understanding report and the 2023 baseline scorecard |
| 3 | Data analyst | The capacity and growth-scenario model |
| 4 | Strategy consultant | Options, recommendation, roadmap, value case |
| 5 | Data analyst | Independent check of every new euro figure and of the growth rule |
| 6 | Data storyteller | Big Idea, storyline, slide outline, graph rationale |
| 7 | Quality and risk lead | Quality gate (10 findings, all fixed) and a recheck (4 more, all fixed) |

The specialists also corrected each other: the analyst showed that an "unexplained" 20 t was rejected batches plus stock build-up, and that a capacity estimate based on the machines' nameplate speed was far too optimistic. The quality gate made the growth claim more cautious ("can probably supply", three conditions, a range instead of a point) and made the headline model runs reproducible.

## Appendix D. Files in this folder

| File | What it is |
|---|---|
| `coffee-case-full-report.md` | This document |
| `storyline.md` | The CEO storyline (version 3, passed the quality gate) |
| `pitch_inputs.md` | All checked numbers, recommendation, roadmap, gates and value case |
| `baseline.md`, `baseline_monthly.csv` | The 2023 KPI scorecard and the monthly table |
| `btdt_baseline.py` | Rebuilds the baseline from the Excel file |
| `btdt_scenarios.py` | The scenario model |
| `btdt_headline_runs.py` | The headline runs (seasonal hours, shelf life, hours per year) |
| `run_output_*.txt` | The output of each script |
