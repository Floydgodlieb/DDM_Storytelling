# Bean There Done That – Presenter Guide

**Pitch title:** *Ready to grow? Not yet. In 12 months: yes.*
**Audience:** the CEO and management team (played by the lecturer)
**Length:** about 16 minutes of presenting + 2 appendix slides for Q&A, within a 30-minute assessment slot

---

## 1. How to run the presentation

| File | Use |
|---|---|
| `Bean_There_Pitch_offline.html` | **Use this one on presentation day.** Works without internet (charts are embedded). |
| `Bean_There_Pitch.html` | Smaller version that loads the chart library online. Good for submitting or emailing. |
| `src/build_deck.py` | Python script that recalculates every number from the Excel file and rebuilds both HTML files. |
| `src/deck_template.html` | The slide design and text. Edit this, then run the script again. |

Open the file in **Chrome or Edge**, then use these controls:

- **→ / Space / PageDown**: next slide. **← / PageUp**: previous slide.
- **F**: full screen. **N**: show or hide speaker notes at the bottom (don't use this while projecting). **Theme** button: switch between light and dark.
- Charts are interactive: hover for exact values and click legend items to hide or show a series.
- Slide 4 (scorecard): click any step. Slide 6: switch between roasts. Slide 15: simulator buttons and sliders.

**Before submitting:**
1. Replace the placeholders on slide 1 (`[Student name 1 · number]`, `Class [__]`). Search for `[Student` in `src/deck_template.html`, then run `python build_deck.py`. You can also edit the two HTML files directly.
2. Check the presentation deadline with your lecturer. The slides list several different dates.

---

## 2. Storyline in one breath

> We threw away 48 t of coffee (**hook**). That's because customers buy with the seasons while we roast at a flat rate (**cause**). The result is waste in summer, a full machine park in autumn, a fragile bean supply and money lost at the doorstep (**4 roadblocks**). There is also capacity hidden in setup time and light-roast quality, and growth potential in the Randstad and in offices (**hope**). So: fix, free, secure, then grow (**advice**). The simulator proves it works (**outcome**), and here is the 12-month plan (**ask**).

This follows Knaflic's structure: a beginning (context and hook), a middle (tension: the roadblocks) and an end (resolution and call to action). Every slide title is a full-sentence takeaway, so the assessor gets the story even from the titles alone.

---

## 3. Running order and speakers

Speaker A opens and closes, B tells the "why", and C covers the operational detail. Change the split if you like, but keep the hand-overs at these points.

| # | Slide | Speaker | Time | Key line |
|---|---|---|---|---|
| 1 | Ready to grow? | A | 0:30 | "Not yet, and in twelve months, yes." |
| 2 | 48,000 kg | A | 1:00 | "The capacity for growth is partly already there. It's in the bin." |
| 3 | The brief + CRISP-DM | A | 1:00 | "Demand was frozen, so 2023 is a clean test." |
| 4 | KPI scorecard (click Stock, Roasting) | A | 1:15 | "Seven steps, four are red." → hand to B |
| 5 | Customers drink like the seasons | B | 1:00 | "658 orders every day, but 38% more coffee in autumn." |
| 6 | We roast like a metronome | B | 1:00 | "Push production: too much in summer, too little in autumn." |
| 7 | Roadblock 1: Waste | B | 1:15 | "Waste is a brand risk as well as a cost." |
| 8 | Roadblock 2: Capacity | B | 1:00 | "One full shift on every machine, every day." → hand to C |
| 9 | Hidden capacity | C | 1:15 | "Before buying a third roaster, win back the lost minutes." |
| 10 | Roadblock 3: Sourcing | C | 1:00 | "10 days of beans left in July." |
| 11 | Roadblock 4: Doorstep | C | 1:15 | "30,725 customers paid for a bug." |
| 12 | Where to grow | C | 1:00 | "6.8 million people in the Randstad barely know us." → hand to A |
| 13 | Verdict | A | 0:45 | "Not ready, but every roadblock is fixable." |
| 14 | Six moves | A | 1:30 | "Fix, free, secure, then grow." → hand to B |
| 15 | Simulator (live demo) | B | 1:30 | Click "change nothing", then "with our plan". |
| 16 | Roadmap + value | B | 1:00 | "≈ €1.67M a year, no third roaster." → hand to A |
| 17 | Close | A | 0:30 | "Last year 48,000 kg in the bin. Next year zero." |
| | **Total** | | **≈ 16:45** | |
| A1 | Explore the data | any | Q&A | Backup for detailed questions |
| A2 | Assumptions & data quality | any | Q&A | Backup for "how reliable is this?" |

**If you need to cut time:** drop slide 3 (say "we followed CRISP-DM" on slide 4) and slide 12. That saves about 2 minutes.

**Live demo tip (slide 15):** practise it. Click **"Grow 20%, change nothing"** first. Pause on the red verdict and the red bars in Sep–Dec. Then click **"Grow 20% with our plan"** and let the verdict turn green. If you have time, drag web shop growth to 40% to show there's still headroom.

---

## 4. Full speaker script

The same text appears in the deck when you press **N**. Use it to rehearse, but don't read it out word for word.

**1 · Title (A).** Good morning. We are [names]. Bean There Done That hired us with one question from the CEO: are we ready to grow next year? Our short answer is on the screen. Not yet, and in twelve months, yes. In the next fifteen minutes we show you why, and what has to happen first.

**2 · Hook (A).** Before we talk about growth, one number. In 2023 the company threw away 48 tonnes of roasted coffee because it expired in the warehouse. At shelf price that's €1.16 million: 6% of everything the roasters produced, and enough to serve every webshop customer for 25 days. A company that can't sell what it already roasts isn't ready to roast more. But there's hope in this number too: part of the capacity we need for growth is already there. It's just in the bin.

**3 · Approach (A).** At the start of 2023 the company froze its customer base. For us as analysts that's a gift: it's a controlled experiment. If the operation struggled with frozen demand, it will struggle more with growth. We followed CRISP-DM. One check made us trust the data: production minus sales minus scrap equals the change in stock, to the kilo, for every roast and every month. Our test for every part of the company was simple: could it take 20% more volume?

**4 · Scorecard (A).** Here is the whole company on one screen: seven steps from the farm to the customer's door, each with a KPI and a target. *(Click Stock.)* 48 tonnes expired. *(Click Roasting.)* Both roasters already run a full shift every day. Sourcing: at one point we had beans for only 10 days. And we lose a million euro a year on parcels. The rest of our story follows the coffee through these red boxes. [B], over to you.

**5 · Seasons (B).** To understand the waste, start with demand. The flat line is the number of web orders per day: 658, every day of the year. That's the customer freeze, perfectly visible. But look at the kilograms. From September to December, and again in February, the same customers order much bigger baskets: 3.5 kilos instead of 2.5. Autumn demand is 38% higher than summer. And it's predictable. It repeats with the calendar.

**6 · Metronome (B).** The bars are what we roast, the line is what we sell. The roasters run like a metronome: about 65 tonnes every month. In spring and summer we roast more than we sell; in autumn, less. *(Click Dark.)* Dark roast is the extreme: in March we roasted 10 tonnes more than we sold.

**7 · Waste (B).** This is where the summer surplus ends up. Stock grows to almost 70 tonnes in May, and from June to August 48 tonnes is written off. But there's a second problem: in May, dark roast stock covered 49 days of sales. Specialty coffee is at its best within about four weeks of roasting, so even the coffee that didn't expire reached customers older than a premium brand should allow. Waste is a quality and brand risk as well as a cost.

**8 · Capacity (B).** Why not simply roast more in autumn? Because the machines are full. The P60 roasts 8.0 hours a day and the Px120 8.5 hours. The packing line, which both share, needs about 8.3. That's one full shift on every machine, every working day. With 20% growth, autumn demand would be about 50% above what one shift can produce. That's the wall. [C]?

**9 · Hidden capacity (C).** There's good news in the roasting log. The Px120 is rated at 480 kilos an hour but achieves 292, and 27% of each cycle is setup: six minutes between batches. Halving that with quick-changeover methods and longer campaigns per roast gives about 15% more capacity for almost no money. Second: light roast. One in twenty light-roast batches is rejected, more than three and a half times as often as the other roasts, spread over weight, colour and profile. That's a recipe problem, not bad luck.

**10 · Sourcing (C).** Upstream, the green beans. We converted bean stock into days of use. The dashed line is a six-week safety level, which is sensible for coffee that travels by sea. Almost every origin dips below it, and at the end of July we had beans for only 10 days in total. Uganda was down to 1,200 kilos. There's no visible reorder rule. In a steady state you get away with it. With growth, one delayed ship stops a roaster.

**11 · Doorstep (C).** Every order band loses money on shipping. PostNL costs €6.75 a parcel, and we charge €4.95 below €55 and nothing above: minus €1 million a year. We also found a bug. The website promises free shipping above €55, but the checkout gives it from five bags. Three 1 kg bags for €69 still pay shipping. That happened 30,725 times, €152,000 charged against our own promise. And 8% of parcels arrive late, evenly spread over the year, which points at the carrier agreement. Mondays get two and a half times the normal volume.

**12 · Where to grow (C).** Once we're ready, where should growth come from? Per inhabitant, Noord- and Zuid-Holland, 6.8 million people, order the least of all provinces. If they bought like the rest of the country, that would be 85,000 more orders a year. And offices: B2B demand is flat all year, so it fills the summer dip instead of the autumn peak. It costs €1.26 per kilo to deliver against €2.28 for a parcel, and our truck already drives to Amsterdam, Rotterdam and The Hague. [A]?

**13 · Verdict (A).** So, four roadblocks, each with evidence and with what 20% growth would do. The most serious is capacity combined with planning: we'd lose about 56 tonnes of sales in autumn while still throwing coffee away in summer. None of these needs a third roaster. They need planning, discipline and a few more hours in the peak.

**14 · Six moves (A).** Our advice is six moves in a fixed order. First, *fix*: roast to demand with monthly planning and at most four weeks of stock; and honour our own promise by fixing the shipping bug and renegotiating with PostNL. Then *free* capacity: halve setup time, fix light roast, and add a second shift only in the six peak months. *Secure* the beans with reorder points and safety stock. Only then *grow*: reopen in spring, starting with offices and the Randstad. Every move has a KPI the CEO can track monthly. [B] will show what it does.

**15 · Simulator (B).** This simulator is built on the 2023 data. As a check, it predicts 38 tonnes of waste for 2023, close to the real 48. *(Click "change nothing".)* Grow 20% and change nothing: demand is above capacity all autumn, and we lose 55 tonnes of sales, about €1.4 million. *(Click "with our plan".)* Same growth with our plan: no lost sales, no expired coffee, and peak load at 93%. Move the slider and the same two roasters can carry around 40% growth.

**16 · Roadmap (B).** The first quarter is about fixing: planning, shipping and bean reorder points. The second frees capacity. The peak shift is recruited in summer and ready for September. Growth starts in spring, so new demand arrives when capacity is free. Stopping the waste and halving the shipping loss is worth about €1.7 million a year, and 20% growth adds €3.6 million in revenue, with no third roaster. Our ask: approve the planning, shipping, changeover and bean moves today, and decide on the peak shift in April.

**17 · Close (A).** So, are we ready to grow? Last year 48 tonnes went in the bin. With these moves, next year that's zero, we serve 20% more customers, and we do it with the same two roasters. Fix, free, secure, then grow. Thank you. We're happy to take your questions.

---

## 5. Q&A preparation

**"How do you know the 48 t is waste and not a data error?"**
Reason code EXP (expired) in the finished-goods sheet: 15 + 10 + 5 t dark, 5 + 7 t medium and 6 t light, in June to August. The mass balance (production − sales − scrap = stock change) closes for every month, so the scrap is consistent with the rest of the data.

**"Why don't you recommend a third roaster?"**
Three cheaper steps come first. Planning removes the summer overproduction, setup reduction plus the light-roast fix gives about 15%, and a peak shift gives +90% hours for six months. The simulator shows this carries about 40% growth. A third roaster becomes relevant beyond that, and the KPIs (peak utilisation > 90%) will tell you when.

**"Isn't a second shift expensive?"**
Only six months a year, and only for the roasting and packing team. Compare it with roughly €1.4M of lost sales at +20% growth without it. We don't have wage data, so we leave the exact cost to the business case, and we recommend deciding in April.

**"How did you calculate machine hours?"**
Batches per day × (setup + run time). We assume cooling overlaps with the next batch. If it doesn't, the machines are even fuller and our conclusion gets stronger.

**"Why 4 weeks of freshness?"**
Specialty roasters generally sell coffee within weeks of roasting, and the 2023 data shows expiry once stock cover went past about 6 weeks. Four weeks is a conservative target that leaves room for transport and the customer's own shelf time.

**"Is the free-shipping bug real?"**
In the data, every order of 5 or more bags ships free and every order below 5 bags pays €4.95, whatever its value. Three 1 kg bags are €68.94–79.50, which is above €55, and they still paid. That covers 30,725 orders and €152,089.

**"Where does the population data come from?"**
CBS figures for 1 January 2023, rounded. That is the only external data we used, and it's marked on the slide.

**"Why is on-time delivery 92% and not 64%?"**
We measured against the actual promise: next working day, excluding weekends and public holidays. Measured in calendar days it would look worse, but that would be unfair to the carrier.

**"What would you do with more data?"**
Get cost prices per roast (to turn shelf value into profit), order timestamps (to test dispatch cut-off times), and which origin goes into which roast (to link bean risk to products). We also found that the packaging bag inventory does not reconcile with sales, so we recommend scanning packaging use (appendix B).

**"Why should growth start with B2B?"**
B2B demand is flat all year, so it fills the summer dip. It's cheaper to deliver (€1.26/kg vs €2.28/kg), and 9 of our 21 office clients are already in the Randstad cities where the webshop is weakest.

---

## 6. Self-check against the assessment form

| Criterion (weight) | Where we cover it |
|---|---|
| In-depth digging of the data (10%) | Mass-balance check, implied bean usage, holiday-aware delivery promise, setup share per machine, the free-shipping bug, orders per inhabitant. Slides 3, 9, 11, 12 and appendix B. |
| Right data used (10%) | All 5 sheets used, plus only one clearly marked external source (CBS population). A source line under every chart. |
| Visuals clear and easy to understand (20%) | One message per slide, takeaway titles, roast colours that match the real coffee, red only for problems, highlighted focus (Knaflic: declutter, focus attention). |
| Visuals attractive, interactive/static (15%) | Interactive HTML deck: hover, clickable KPI chain, roast toggle, live simulator, data explorer. Consistent design and dark mode. |
| Decisions improve operations (20%) | Six moves, each with a KPI and a timing; simulator shows the outcome; value of about €1.67M a year plus growth headroom. Slides 14–16. |
| Story complete and convincing for the stakeholder (25%) | Hook, tension (4 roadblocks), resolution, outcome, concrete ask, and a close that calls back to the hook. Written for the CEO's own question. |

Remember: a score of 1 on any criterion means a resit, so rehearse the full run-through at least twice, including the simulator demo.
