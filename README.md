# Cartiva — E-Commerce Product, Cohort & Funnel Analytics

> **Project Status: Completed & Production-Ready (100% Deployed)**
>
> The end-to-end analytics pipeline—spanning the **Modular Python ETL**, **MySQL Semantic Views**, **TMDL Power BI Star Schema**, and the **3-Page Executive & Diagnostic Power BI Application** (`Overview`, `Customers & Cohort Retention`, and `Funnel Diagnostics`)—is fully completed and operational.

## Executive Story Brief: The Leaky Bucket Paradox

**Cartiva** had no problem attracting attention. Thousands of visitors flooded the platform across **25,000+ browsing sessions**, generating **\$27M in revenue** and making the business look like a thriving e-commerce success on the surface.

Yet behind the scenes, the platform was bleeding at both ends of the customer journey—leaving **87.49% of the entire customer base in an unsafe purchasing state** (`Never Bought`, `Churned`, or `At-Risk`):

* **The Visitors Who Never Buy:** Massive waves of shoppers actively browsed product pages and even loaded their carts, only to vanish right before completing their order—leaving **56.58% of all registered users with zero purchases**. Yet **49.77% of all users remain Active Browsers** (with `Never Bought` representing **61%** of active traffic), sitting on a massive **+\$5.52M (+20.4%) untapped revenue goldmine**.

* **The Buyers Who Never Return:** Worse still, converting a visitor wasn't enough. Even the customers who completed a purchase—including top-spending **VIPs**—were quietly walking away after their orders, churning at nearly **44%** across a "Zero-Loyalty Ecosystem" and never coming back.

Leadership didn't need another dashboard showing total sales; they needed to know **why shoppers were abandoning the funnel** and **why buyers weren't sticking around**. By engineering an end-to-end analytics pipeline (`Python ETL` → `MySQL Window Functions` → `Power BI Star Schema`) and grouping users into **behavioral, acquisition, and spending cohorts**, this project diagnoses the exact friction points causing funnel leakage, empirically debunks false marketing assumptions, and exposes the retention gaps draining customer lifetime value.

## 1. The Business Story: Why "\$27M in Revenue" Was Hiding a Silent Crisis

On paper, **Cartiva** looked like an e-commerce success story. Top-line reports showed **\$27M in total revenue** across **4,000+ completed orders**, an impressive **\$6.04K Average Order Value (AOV)**, and a **36.88% Buyer Conversion Rate**, with monthly revenue surging exponentially to **\$12.5M in June**.

However, beneath this rapid top-line growth, unit economics were quietly deteriorating:

1. **The Conversion Black Hole & Macro Risk:** Marketing was pouring budget into traffic acquisition across **25,000+ sessions**, yet **87.49% of the customer base was commercially unsafe**—including **56.58% of registered users (5,658 profiles)** who had never completed a single purchase.

2. **Invisible Funnel Friction & Price/Loyalty Myths:** Leadership knew visitors were leaving—especially **890 dead accounts from Paid Search & Paid Social**—and initially blamed expensive `Premium` product pricing or cold `New Visitor` traffic, lacking visibility into *where* intent actually evaporated across the shopping journey (`View Item` → `Add to Cart` → `Begin Checkout` → `Purchase`).

3. **The "Zero-Loyalty" Trap:** Standard reporting lumped all inactive users together. The business could not distinguish between a permanently dead account and an active window-shopper (**61% of Active Browsers are Non-Buyers**, and **25% of Churned Buyers are still actively browsing**), nor did it realize that its highest-spending VIPs were quietly abandoning the platform at the exact same rate (\~44%) as budget shoppers.

### Mission Objective

Instead of building another static sales tracker, **Cartiva** was engineered as an end-to-end product analytics and behavioral diagnostic system. By combining a **Python ETL pipeline**, **MySQL Window Functions**, and a **TMDL-structured Power BI Semantic Model**, this project groups users into actionable **behavioral, acquisition, and spending cohorts**—using those cohorts to isolate the exact root causes of funnel leakage, formulate testable **A/B Testing hypotheses**, recover wasted ad spend, and halt structural customer churn.

## 2. Dashboard Architecture & UI Previews

Designed strictly around *Storytelling with Data* principles (Cole Nussbaumer Knaflic), the UI eliminates visual clutter (no scrollbars, gridlines, or redundant axes), enforces a purposeful pre-attentive color hierarchy (slate navy, sage olive gradients, baseline neutral grays `#A6A6A6`, and high-alert warning red `#D93836` reserved strictly for critical drop-offs), and uses **active, conclusion-driven chart titles** to guide executive attention directly to commercial bottlenecks.

### Modular 3-Page SaaS Application Layout

The report is architected as an interactive 3-page application with a persistent left navigation rail, transparent hover-state action buttons, and standardized analytical containers:

| Report Page | Status | Primary Commercial & Product Questions Answered | 
| ----- | ----- | ----- | 
| **1. Overview** | **Completed** | How are we performing against macro KPIs? Where is the steepest macro funnel drop-off occurring? What is the true health of our customer base when crossing purchase history with live browsing activity? | 
| **2. Customers** | **Completed** | How do our user cohorts behave across the Dual-Churn Matrix (`Purchase Churn × Activity Churn`)? How much historical LTV is at risk due to Structural VIP Churn? Which acquisition channels generate permanently dead accounts? | 
| **3. Funnel** | **Completed** | Where exactly do we lose potential buyers across the checkout flow (`50.17% Cart Abandonment`, `37.46% View-to-Cart Drop-off`, `4.42% Purchase Failure`)? Does checkout friction stem from product price tiers (`Core` vs. `Entry` vs. `Premium`) or visitor familiarity (`New` vs. `Returning`)? Which product categories exceed the `46.5%` consideration drop-off benchmark? | 

### Page 3 Preview: Funnel Diagnostics Dashboard

## 3. Analytical Methodologies & Cohort-Driven Diagnostics

Cartiva moves beyond surface-level reporting by applying eight specialized analytical frameworks—using **Cohort Grouping** and **Advanced DAX Context Manipulation** to diagnose funnel leakage and retention decay:

| Analysis Type | Why It Was Used (Why) | Implementation Details (How) | Key Findings / Indicators (Findings) | Commercial Actionability (Business Value) | 
| ----- | ----- | ----- | ----- | ----- | 
| **Descriptive Analysis** | Establish an executive commercial baseline before investigating causal mechanics. | Synthesized top-level KPI cards (Revenue, Orders, AOV, Buyer Conversion %) alongside monthly trend lines and traffic distributions in Power BI. | Revenue reached **\$27M** across **4K orders** with a **\$6.04K AOV** and **36.88% Buyer Conversion %**, demonstrating rapid revenue acceleration peaking in June (**\$12.5M**). | Aligns executive leadership on baseline commercial velocity and highlights whether growth is driven by order volume or basket size. | 
| **Cohort Analysis (Behavioral & Acquisition Cohorts)** | Group users into distinct shared-trait cohorts to uncover *who* is experiencing funnel leakage and *why* retention decays post-acquisition. | Segmented the 10,000-user base into **Onboarding Cohorts** (`New Visitors` vs. `Returning`), **Acquisition Channel Cohorts** (`Paid Search`, `Paid Social`, `Organic`, `Referral`), **Spending Tiers** (`Budget`, `Mid-Tier`, `VIP`), and **Recency Cohorts**. | Funnel diagnostics proved that **Returning Visitors abandon checkout just as often as New Visitors (`50.78%` vs. `49.27%`)**, proving a systemic UX flaw; meanwhile, `Paid Search` & `Paid Social` cohorts generate **44.7% (890 accounts)** of permanently dead non-buyers, and `VIP` cohorts exhibit a **43.9% structural churn rate**. | Replaces blanket assumptions with targeted interventions—fixing systemic checkout UX for all users while reallocating paid ad spend toward conversion-optimized objectives. | 
| **Funnel & Stage-Leakage Analysis** | Quantify leakage across the user journey and pinpoint the exact screen where purchase intent evaporates. | Mapped 25,000 sessions into a hierarchical funnel sequence (`View Item` → `Add to Cart` → `Begin Checkout` → `Purchase`); engineered stage-to-stage drop-off DAX measures and benchmark lines. | Primary leakage walls occur at: (1) **Begin Checkout / Cart Abandonment (`50.17%` drop-off)**, (2) **Add to Cart / Consideration Gap (`37.46%` overall store drop-off; `19.99%` initial view drop-off)**, and (3) a technical **Purchase Failure Rate (`4.42%` session-level / `19.78%` final checkout step loss)**. | Directs engineering and UX **A/B testing** toward the checkout initiation wall, shipping calculators, and payment gateway reliability to recover lost sales. | 
| **Cross-Grain Price Tier Diagnostics (DAX Lineage)** | Empirically test whether cart abandonment is driven by expensive `Premium` catalog pricing. | Solved GA4-style event granularity limits (where `begin_checkout` logs at the session level without a `product_id`) by engineering virtual tables via `CALCULATETABLE(VALUES(Fact_Events[session_id]))` and `REMOVEFILTERS(Dim_Products)` to track cart sessions across stages. | **Debunked the "Price Shock" myth across the entire store:** Checkout friction hits all price tiers equally—**Core Assortment (`50.33%`)**, **Entry-Level Assortment (`50.31%`)**, and **Premium Assortment (`49.25%`)** all suffer an identical \~50% checkout drop-off. | Eliminates commercial guesswork; proves that discounting `Premium` products will not fix cart abandonment, shifting focus to checkout flow simplification. | 
| **Category Consideration Benchmarking** | Isolate which product categories suffer from severe product-page hesitation (`View Item` → `Add to Cart`) without misleading stakeholders. | Evaluated all 10 catalog categories (ranging from `45.17%` to `48.73%` drop-off against the `37.46%` multi-category store average); applied a **46.5% Category Average Benchmark Line** to isolate above-average friction categories without visual scrollbar clutter. | Revealed a systemic store-wide consideration gap (`45%–49%`), with 4 key categories exceeding the **46.5% category average**: **Furniture (`48.73%`)**, **Beauty (`47.73%`)**, **Sports (`46.90%`)**, and **Food (`46.60%`)**. | Guides merchandising teams to prioritize PDP enhancements (sizing guides, AR previews, ingredient/trust badges, and user reviews) starting with `Furniture` and `Beauty`. | 
| **Dual-Layer Churn Analysis** | Distinguish between customers who stopped buying versus those who stopped engaging with the platform altogether. | Formulated a 2D retention matrix crossing **Purchase Churn** (SQL-calculated days since last order vs. median cycle benchmark) with **Activity Churn** (DAX recency of last web session event). | While **87.49% of users are in an unsafe purchasing state**, crossing with live activity proves **49.77% (4,977 users) are Active Browsers**—where **61% (3,047 users) are Active Non-Buyers** and **25% of Churned Buyers are still active on-site**, while isolating **2,897 permanently dead accounts**. | Unlocks a projected **+\$5.52M (+20.4% revenue lift)** by converting 30% of Active Non-Buyers, saves **31.5% in wasted retargeting spend**, and prioritizes low-CAC win-back for the 25% active churned buyers. | 
| **Customer Segmentation** | Avoid generic marketing by treating non-buyers, active buyers, and high-LTV VIPs as distinct populations. | Segmented users in SQL/DAX across two axes: Lifecycle Status (`Never Bought`, `Active`, `At-Risk`, `Churned`) and Spending Quartile Tiers (`Budget`, `Mid-Tier`, `VIP`). | Exposed a "Zero-Loyalty Ecosystem" (\~44% uniform churn): **65.9% of VIPs (608 top buyers)** and **66.8% of Mid-Tier buyers (1,233 users)** are currently either `Churned` or `At-Risk`, threatening two-thirds of historical revenue. | Enables targeted lifecycle email sequences, dynamic free-shipping thresholds by tier, and urgent VIP concierge win-back workflows. | 
| **Order Lifecycle Analysis** | Evaluate first-purchase acquisition friction separately from repeat buyer loyalty velocity. | Tagged transactions in `vw_fact_sales_enriched.sql` (`order_lifecycle_tag`) into: `Immediate First Purchase`, `Delayed First Purchase` (multi-session consideration), and `Repeat Purchase` by comparing `session_start` to `first_completed_date`. | Initial transactions are predominantly **Delayed First Purchases** requiring multi-session comparisons and facing a **2.39% dead-user order failure rate**, whereas **Repeat Purchases convert at a significantly faster velocity and higher AOV**. | Proves that breaking first-order friction is the ultimate LTV catalyst; mandates 48-hour consideration retargeting and immediate service recovery for failed orders. | 

## 4. Deep-Dive Analytical Findings: How Cohort Segmentation Exposed the Leakage

Every insight generated by Cartiva is structured into confirmed quantitative evidence, data-backed hypotheses, and commercial actionability:

### Finding 1: The Systemic 50% Checkout Wall (Universal Across Visitor Types & Price Tiers)

* **The Observation:** Over half of high-intent carts (**50.17% Cart Abandonment Rate**) are abandoned at the `Begin Checkout` step. Leadership initially hypothesized that this drop-off was driven either by unfamiliar `New Visitors` or sticker shock on `Premium Assortment` items. Empirical Funnel Diagnostics disproved both assumptions.

* **The Cohort & Diagnostic Evidence:**

  * **Returning Visitors Abandon Checkout as Often as New Ones:** Slicing checkout drop-off by visitor familiarity reveals that **Returning Visitors (`50.78%` drop-off)** abandon their carts at virtually the exact same rate as **New Visitors (`49.27%` drop-off)** (while isolated single-session lost cohorts spike to `78.89%`). Familiarity with the brand does not protect a user from checkout friction.

  * **Checkout Friction Hits All Price Tiers Equally:** By engineering a cross-grain DAX measure (`Tier Checkout Drop-off`) that tracks session lineage from product-level `add_to_cart` events to session-level `begin_checkout` events, we proved that drop-off is completely invariant to product price:

    * **Core Assortment:** `50.33%` checkout drop-off

    * **Entry-Level Assortment:** `50.31%` checkout drop-off

    * **Premium Assortment:** `49.25%` checkout drop-off

  * **The 4.42% Purchase Failure Anomaly:** Even when users survive checkout initiation, **4.42%** of purchasing sessions (and **2.39%** of permanently lost non-buyers) click `Purchase` without a completed order logging in `Fact_Sales`—pointing to payment gateway timeouts or validation errors.

* **Commercial Action ("The Pill"):**

  1. **Fix the Systemic Checkout UX:** Because the \~50% drop-off hits Returning and New users equally across all price tiers, the bottleneck is structural (e.g., surprise flat-rate shipping fees revealed late in checkout, slow page loads, or clunky multi-step forms). Implement upfront shipping calculators inside the slide-out cart drawer and streamline payment steps via **1-Click Checkout (Apple Pay / Google Pay / BNPL)**.

  2. **Automated Service Recovery:** Deploy real-time webhook alerts and an automated apology voucher + cart restoration email for the **4.42% failed purchase sessions** so technical payment glitches never permanently burn acquired traffic.

### Finding 2: The Store-Wide Consideration Gap (45%–49%) & Paid Traffic Leakage

* **The Observation:** Before users even reach the cart, **37.46%** of total store sessions that view products fail to add a single item to their cart. However, when evaluating individual product categories, category-level consideration drop-off ranges tightly between **45.17% and 48.73%** due to multi-category browsing behavior (where a shopper views multiple departments in one session but only adds to cart from one).

* **The Cohort Evidence:**

  * **Isolating Above-Average Friction Categories (>46.5%):** Rather than misleading management by displaying a truncated chart without context, establishing the **46.50% Category Average Benchmark** isolates the four specific departments driving above-average hesitation: **Furniture (`48.73%`)**, **Beauty (`47.73%`)**, **Sports (`46.90%`)**, and **Food (`46.60%`)**.

  * **The Paid Traffic Checkout Collapse:** Tracing the **890 permanently dead accounts** acquired via `Paid Search` (489 users) and `Paid Social` (401 users) revealed that they actually pass the product consideration stage well (`15.97%–18.18%` view drop-off) and add items to their carts (`Core: 379 users`, `Entry-Level: 212 users`, `Premium: 195 users`), only to collapse at **`Begin Checkout` (`76.92%–79.76%` drop-off)** and **`Purchase` (`81.58%` Entry-Level drop-off)**.

* **Commercial Action & A/B Testing Roadmap ("The Pill"):**

  1. **PDP Merchandising Upgrades (Furniture & Beauty):** Reduce the \~48% consideration gap in `Furniture` and `Beauty` by adding interactive dimension/sizing visualizers, explicit return-policy badges, and verified customer photo reviews directly beneath the "Add to Cart" button.

  2. **A/B Test (Guest Checkout & Free-Shipping Thresholds):** Test a **1-Click Guest Checkout** flow and a dynamic *"Add \$X for Free Shipping"* progress bar for `Paid Social` and `Paid Search` traffic to compress their \~80% checkout initiation wall.

### Finding 3: The Dual-Churn Matrix, The +\$5.52M Hidden Gem & Structural VIP Attrition

* **The Observation:** While **87.49% of the total customer base** sits in an unsafe purchasing zone, crossing transactional status with live web activity uncovers a massive, zero-CAC revenue goldmine alongside an urgent VIP loyalty crisis.

* **The Cohort Evidence:**

  * **The +\$5.52M Hidden Gem (`Active Browsers × Never Bought`):** The Dual-Churn Matrix proves that **49.77% (4,977 users)** of the entire database are **Active Browsers**. Crucially, **61% of these active users (3,047 profiles) are `Never Bought` window-shoppers** whose acquisition cost is already sunk. Converting just **30%** of this active cohort at the baseline **\$6,040 AOV** yields a **+20.4% surge in total company revenue**:
    

    $$
    \text{Projected Revenue Lift} = (3,047 \text{ Active Non-Buyers} \times 30\%) \times \$6,040 \text{ AOV} = 914 \text{ New Buyers} \times \$6,040 = \mathbf{+\$5,520,560}
    $$

  * **The Low-Hanging Fruit (`25% Active Churned`):** Exactly **25% of historically `Churned` buyers are still `Active Browsers`** (408 active past buyers overall) who regularly visit the site. Re-activating these brand-familiar past buyers requires a fraction of cold acquisition CAC.

  * **Structural VIP Churn ("Zero-Loyalty Ecosystem"):** Crossing **Spending Tiers × Churn Status** reveals that Cartiva operates without retention differentiation—churn is flat at **\~44% across all brackets**. Specifically, **VIPs churn at 43.9%**, with combined Churned and At-Risk VIPs reaching **65.9% (608 VIPs)**, mirrored by **66.8% in the Mid-Tier (1,233 users)**—putting **two-thirds of historical baseline revenue** in immediate jeopardy.

* **Commercial Action ("The Pill"):**

  1. **Capture the +\$5.52M Gem:** Trigger automated in-session first-order incentives (e.g., *Free Express Shipping + First-Order Guarantee*) for the **3,047 Active Non-Buyers**.

  2. **Low-CAC Win-Back & Ad Savings:** Suppress the **2,897 permanently dead accounts** from paid retargeting to **save 31.5% in ad spend**, reinvesting those funds into personalized "Welcome Back" credits for the **25% Active Churned** cohort.

  3. **VIP Loyalty Program:** Halt the 65.9% VIP attrition by launching a tiered **VIP Concierge & Loyalty Program** (automatic free shipping, priority inventory access, and milestone rewards) for top-tier and Mid-Tier buyers.

## 5. Project Implementation Status

All core data engineering, semantic modeling, and business intelligence deliverables are completed:

```
├── [COMPLETED / PRODUCTION-READY]
│   ├── Modular Python ETL pipeline with data standardization & schema validation
│   ├── Star-Schema Data Warehouse tables deployed in MySQL 8.0
│   ├── Enriched analytical SQL views (User lifecycle, 6-stage Funnel sequencing, Sales lifecycle)
│   ├── Enterprise Power BI Project (.pbip) with TMDL semantic model definitions
│   ├── Core & Advanced DAX measure library:
│   │   ├── Cross-grain session lineage (CALCULATETABLE + VALUES + REMOVEFILTERS)
│   │   ├── Dual-Churn Matrix & Active Non-Buyer revenue lift projections
│   │   └── Stage-by-stage funnel drop-off & category consideration benchmarks
│   ├── Page 1: Executive Overview Dashboard (Macro KPIs, Trends, Funnel Drop-offs, Churn Split)
│   ├── Page 2: Customers & Cohort Retention Dashboard (Dual-Churn Matrix, VIP Attrition, CAC Bleed)
│   ├── Page 3: Funnel Diagnostics Dashboard (Stage Leakage, Price Tier Parity, Visitor Cohorts, Category Benchmarks)
│   ├── Interactive Cross-Page Navigation Rail with Hover Effects
│   └── Executive Documentation PDFs (Strategic Blueprint & Important Findings Executive Brief)
│
└── [FUTURE PHASE 2 EXTENSIONS]
    ├── Device & Platform Telemetry Slicers (Mobile vs. Desktop Checkout UX Isolation)
    └── A/B Test Statistical Significance Calculator for Guest Checkout & Free-Shipping Experiments

```

## 6. Data Architecture, Star Schema & Advanced DAX Engineering

Cartiva is architected as a multi-fact **Star Schema** in Power BI, purposefully separating high-frequency behavioral web events from invoice-level financial transactions:

```
                        ┌──────────────────┐
                        │   Dim_Sessions   │
                        └─────────┬────────┘
                                  │ (1:N)
        ┌─────────────────────────┼─────────────────────────┐
        │ (1:N)                   │                         │ (1:N)
┌───────┴────────┐       ┌────────▼───────┐        ┌────────▼───────┐
│ Dim_Customers  ├──────►│  Fact_Events   │        │   Fact_Sales   │◄───────┐
└───────┬────────┘ (1:N) └────────────────┘        └────────────────┘ (N:1)  │
        │ (1:N)                                                              │
        └────────────────────────────────────────────────────────────┐       │
                                                                     │       │
                                                            ┌────────┴───────┴┐
                                                            │  Dim_Products   │
                                                            └─────────────────┘

```

### Why Separate `Fact_Events` and `Fact_Sales`?

* **Granularity Isolation:** `Fact_Events` captures clickstream progression (`view_item`, `add_to_cart`, `begin_checkout`, `purchase`) at the **session-timestamp grain** across 25,000 sessions. `Fact_Sales` records completed monetary transactions at the **order-item line grain**.

* **Query Performance & DAX Accuracy:** Merging clickstream logs with order financials into a single flat table causes severe row inflation and distorts conversion denominators. Isolating them allows DAX measures to seamlessly cross-filter behavioral cohorts against actual revenue yield via shared dimensions (`Dim_Customers`, `Dim_Sessions`, `Dim_Products`).

### Solving the GA4 Session-Level Granularity Challenge in DAX

In standard event-stream schemas (such as Google Analytics 4 and Cartiva's `Fact_Events`), product-level attributes (`product_id`, `Price Tier`) are logged during `view_item` and `add_to_cart` events, whereas `begin_checkout` is logged as a **session-level event** (`product_id = NULL`). Naive funnel slicing by `Price Tier` falsely reports a `100%` drop-off at checkout because the product filter context eliminates session-level checkout rows.

To solve this, we engineered a **Virtual Table Data-Lineage DAX Pattern** that captures the exact `session_id` cohort that added a specific Price Tier to their cart, then strips the product dimension filter via `REMOVEFILTERS` while preserving session lineage:

```
Tier Checkout Drop-off = 
VAR CartSessionsForTier = 
    CALCULATETABLE(
        VALUES(Fact_Events[session_id]),
        Fact_Events[event_type] = "add_to_cart"
    )
VAR CartCount = COUNTROWS(CartSessionsForTier)
VAR CheckoutCount = 
    CALCULATE(
        DISTINCTCOUNT(Fact_Events[session_id]),
        Fact_Events[event_type] = "begin_checkout",
        CartSessionsForTier,
        REMOVEFILTERS(Dim_Products)
    )
RETURN
    DIVIDE(CartCount - CheckoutCount, CartCount, 0)

```

## 7. SQL Semantic Layer & Engineering Logic

Before data reaches Power BI, complex cohort classifications and window sequencing are pushed upstream into three MySQL analytical views:

1. [**`vw_dim_users_enriched.sql`**](SQL/vw_dim_users_enriched.sql) **— Customer Cohorts, LTV Tiers & Churn Benchmarks:**

   * Aggregates lifetime orders, historical spend (LTV), and days elapsed since last purchase/activity per user.

   * Computes a dynamic global **median inter-purchase cycle benchmark** across the customer base.

   * Classifies users into **Purchase Churn Cohorts** (`Active`, `At-Risk`, `Churned`, `Never Bought`), **Activity Churn Cohorts** (`Activity Active` vs. `Activity Churned`), and **Spending Tiers** (`Budget`, `Mid-Tier`, `VIP`).

2. [**`vw_fact_events_enriched.sql`**](SQL/vw_fact_events_enriched.sql) **— 6-Stage Funnel Mapping & Window Sequencing:**

   * Standardizes raw clickstream payloads into a strict 6-stage hierarchical funnel taxonomy.

   * Applies `ROW_NUMBER() OVER (PARTITION BY session_id ORDER BY event_timestamp)` and `LAG()` window functions to reconstruct exact in-session user pathways and measure stage-to-stage dwell times.

3. [**`vw_fact_sales_enriched.sql`**](SQL/vw_fact_sales_enriched.sql) **— Order Lifecycle Classification:**

   * Evaluates transaction timestamps (`first_completed_date`) relative to user onboarding and `session_start` history.

   * Segments orders via `order_lifecycle_tag` into `Immediate First Purchase` (single-session conversion), `Delayed First Purchase` (multi-session consideration cohort), and `Repeat Purchase` (proving accelerated repeat velocity and higher AOV).

## 8. Modular Python ETL Pipeline

Data ingestion and normalization are automated through a clean, modular Python pipeline located in the [`Python/`](Python) directory:

```
Operational DB  ──► [data_extraction.py] ──► [Data_cleaning.py] ──► [data_loading.py] ──► MySQL Analytics Warehouse

```

* **Extraction (`data_extraction.py`):** Streams raw operational tables from MySQL using pooled `SQLAlchemy` connections.

* **Transformation & Cleaning (`Data_cleaning.py`):**

  * Normalizes fragmented UTM/traffic tags into standardized acquisition cohorts (e.g., consolidating raw social referrals into `Paid Social`).

  * Resolves missing timestamps, standardizes date/time partitions, imputes missing catalog categories, and validates pricing integrity.

* **Warehouse Loading (`data_loading.py`):** Upserts cleaned dimension and fact tables into the MySQL analytics schema with strict referential integrity.

* **Orchestration (`main.py`):** Single-command runner that executes the end-to-end Extract-Transform-Load sequence.

## 9. How to Reproduce & Run the Project

### Prerequisites

* **Python 3.10+**

* **MySQL Server 8.0+**

* **Power BI Desktop** (with `.pbip` Power BI Project developer mode enabled)

### Step 1: Clone the Repository

```
git clone https://github.com/ramadanabdelrahmannasser-hue/Cartiva.git
cd Cartiva

```

### Step 2: Execute the Python ETL Pipeline

```
pip install -r Python/requirements.txt
python Python/main.py

```

*(You will be securely prompted for your local MySQL credentials to initialize and populate the warehouse).*

### Step 3: Deploy the SQL Analytical Views

Execute the semantic views in your MySQL environment in the following order:

```
mysql -u root -p warehouse_db < SQL/vw_dim_users_enriched.sql
mysql -u root -p warehouse_db < SQL/vw_fact_events_enriched.sql
mysql -u root -p warehouse_db < SQL/vw_fact_sales_enriched.sql

```

### Step 4: Launch the Power BI Project (`.pbip`)

Double-click `Cartiva.pbip` to open the semantic model and report canvas in Power BI Desktop, then click **Refresh** to load the enriched views.

## 10. Repository Structure

```
.
├── Cartiva.pbip                     # Power BI Project entry point (Git-friendly BI format)
├── Cartiva.Report/                  # Power BI visual layout, custom JSON themes & 3-page definitions
├── Cartiva.SemanticModel/           # Power BI semantic data model & DAX library (TMDL format)
├── Dashboard Designs/               # UI screenshots, layout grids, and wireframes
│   ├── Cartiva_Overview_Dashboard.jpg
│   ├── Cartiva_Customers_Dashboard.jpg
│   ├── Cartiva_Funnel_Dashboard.jpg
│   ├── Cartiva_Overview_Layout.jpg
│   └── Cartiva_Overview_Wireframe.png
├── Documentation/                   # Deep-dive executive blueprints & strategic documentation
│   ├── Important_Findings.pdf
│   ├── Cartiva_Project_Summary_and_Key_Insights.pdf
│   └── Cartiva_Strategic_Funnel_and_Retention_Blueprint.pdf
├── Python/                          # Modular Python ETL pipeline codebase
│   ├── main.py                      # Pipeline orchestrator & entry point
│   ├── data_extraction.py           # MySQL extraction module
│   ├── Data_cleaning.py             # Data standardization & cohort tag normalization
│   ├── data_loading.py              # Star-schema warehouse loader
│   ├── database.py                  # SQLAlchemy connection engine helper
│   └── requirements.txt             # Python environment dependencies
└── SQL/                             # Enriched analytical MySQL views
    ├── vw_dim_users_enriched.sql    # User cohorts, LTV tiers & churn benchmarks
    ├── vw_fact_events_enriched.sql  # 6-stage funnel mapping & window sequencing
    └── vw_fact_sales_enriched.sql   # Order lifecycle classification

```