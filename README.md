# Cartiva — E-Commerce Product, Cohort & Funnel Analytics

![Cartiva Overview Dashboard](Dashboard%20Designs/Cartiva_Overview_Dashboard.jpg)

> **Project Status: Active Development**
>
> The **Executive Overview** and **Customers & Cohort Retention** dashboards, SQL semantic layer, and Python ETL pipeline are fully deployed and operational. The final deep-dive diagnostic view (**Funnel Diagnostics**) is actively being finalized in Power BI.

---

## Executive Story Brief: The Leaky Bucket Paradox

**Cartiva** had no problem attracting attention. Thousands of visitors flooded the platform across **25,000+ browsing sessions**, generating **\$27M in revenue** and making the business look like a thriving e-commerce success on the surface. 

Yet behind the scenes, the platform was bleeding at both ends of the customer journey—leaving **87.49% of the entire customer base in an unsafe purchasing state** (`Never Bought`, `Churned`, or `At-Risk`):
- **The Visitors Who Never Buy:** Massive waves of shoppers actively browsed product pages and even loaded their carts, only to vanish right before completing their order—leaving **56.58% of all registered users with zero purchases**. Yet **49.77% of all users remain Active Browsers** (with `Never Bought` representing **61%** of active traffic), sitting on a massive **+\$5.52M (+20.4%) untapped revenue goldmine**.
- **The Buyers Who Never Return:** Worse still, converting a visitor wasn't enough. Even the customers who completed a purchase—including top-spending **VIPs**—were quietly walking away after their orders, churning at nearly **44%** across a "Zero-Loyalty Ecosystem" and never coming back.

Leadership didn't need another dashboard showing total sales; they needed to know **why shoppers were abandoning the funnel** and **why buyers weren't sticking around**. By engineering an end-to-end analytics pipeline (`Python ETL` → `MySQL Window Functions` → `Power BI Star Schema`) and grouping users into **behavioral, acquisition, and spending cohorts**, this project diagnoses the exact friction points causing funnel leakage, empirically debunks false marketing assumptions, and exposes the retention gaps draining customer lifetime value.

---

## 1. The Business Story: Why "\$27M in Revenue" Was Hiding a Silent Crisis

On paper, **Cartiva** looked like an e-commerce success story. Top-line reports showed **\$27M in total revenue** across **4,000+ completed orders**, an impressive **\$6.04K Average Order Value (AOV)**, and a **36.88% Buyer Conversion Rate**, with monthly revenue surging exponentially to **\$12.5M in June**.

However, beneath this rapid top-line growth, unit economics were quietly deteriorating:

1. **The Conversion Black Hole & Macro Risk:** Marketing was pouring budget into traffic acquisition across **25,000+ sessions**, yet **87.49% of the customer base was commercially unsafe**—including **56.58% of registered users (5,658 profiles)** who had never completed a single purchase.

2. **Invisible Funnel Friction & Paid Traffic Myths:** Leadership knew visitors were leaving—especially **890 dead accounts from Paid Search & Paid Social**—and initially blamed expensive `Premium` product pricing, lacking visibility into *where* intent actually evaporated across the 6-stage shopping journey (`Session Start` → `Purchase`).

3. **The "Zero-Loyalty" Trap:** Standard reporting lumped all inactive users together. The business could not distinguish between a permanently dead account and an active window-shopper (**61% of Active Browsers are Non-Buyers**, and **25% of Churned Buyers are still actively browsing**), nor did it realize that its highest-spending VIPs were quietly abandoning the platform at the exact same rate (~44%) as budget shoppers.

### Mission Objective

Instead of building another static sales tracker, **Cartiva** was engineered as an end-to-end product analytics and behavioral diagnostic system. By combining a **Python ETL pipeline**, **MySQL Window Functions**, and a **TMDL-structured Power BI Semantic Model**, this project groups users into actionable **behavioral, acquisition, and spending cohorts**—using those cohorts to isolate the exact root causes of funnel leakage, formulate testable **A/B Testing hypotheses**, recover wasted ad spend, and halt structural customer churn.

## 2. Dashboard Architecture & UI Previews

Designed around *Storytelling with Data* principles, the UI eliminates visual clutter, enforces a cohesive custom color hierarchy (slate navy, sage olive gradients, and high-alert coral red reserved strictly for critical drop-offs), and guides executive attention directly to commercial bottlenecks.

### Overview UI Layout & Wireframe Architecture

The report is architected as a modular 3-page SaaS application with a persistent left navigation rail and standardized analytical containers:

![Cartiva Overview Layout](Dashboard%20Designs/Cartiva_Overview_Layout.jpg)

![Cartiva Customer Intelligence](Dashboard%20Designs/Cartiva_Customer_Intelligence.png)

| Report Page | Status | Primary Commercial & Product Questions Answered | 
| ----- | ----- | ----- | 
| **1. Overview** | **Completed** | How are we performing against macro KPIs? Where is the steepest funnel drop-off occurring? What is the true health of our customer base when crossing purchase history with live browsing activity? | 
| **2. Customers** | **Completed** | How do our user cohorts behave across the Dual-Churn Matrix (`Purchase Churn × Activity Churn`)? How much historical LTV is at risk due to Structural VIP Churn? Which acquisition channels generate permanently dead accounts? | 
| **3. Funnel** | **In Progress** | How do specific user cohorts (New vs. Returning, Price Tiers, and Traffic Channels) experience funnel leakage? Why did the "Premium Price Shock" hypothesis fail, and what is causing the ~80% Paid Traffic collapse at `Begin Checkout`? | 

## 3. Analytical Methodologies & Cohort-Driven Diagnostics

Cartiva moves beyond surface-level reporting by applying eight specialized analytical frameworks—using **Cohort Grouping** as the primary lens to diagnose funnel leakage and retention decay:

| Analysis Type | Why It Was Used (Why) | Implementation Details (How) | Key Findings / Indicators (Findings) | Commercial Actionability (Business Value) | 
| ----- | ----- | ----- | ----- | ----- | 
| **Descriptive Analysis** | Establish an executive commercial baseline before investigating causal mechanics. | Synthesized top-level KPI cards (Revenue, Orders, AOV, Buyer Conversion %) alongside monthly trend lines and traffic distributions in Power BI. | Revenue reached **\$27M** across **4K orders** with a **\$6.04K AOV** and **36.88% Buyer Conversion %**, demonstrating rapid revenue acceleration peaking in June (**\$12.5M**). | Aligns executive leadership on baseline commercial velocity and highlights whether growth is driven by order volume or basket size. | 
| **Cohort Analysis (Behavioral & Acquisition Cohorts)** | Group users into distinct shared-trait cohorts to uncover *who* is experiencing funnel leakage and *why* retention decays post-acquisition. | Segmented the 10,000-user base into **Onboarding Cohorts** (`New Visitors` vs. `Returning`), **Acquisition Channel Cohorts** (`Paid Search`, `Paid Social`, `Organic`, `Referral`), **Spending Tiers** (`Budget`, `Mid-Tier`, `VIP`), and **Recency Cohorts**. Cross-tabulated each cohort against stage-by-stage funnel drop-offs. | Cohort isolation proved that funnel leakage is not uniform: `New Visitor` cohorts suffer a **78.89% Cart-to-Checkout drop-off** (vs. 50.17% overall); `Paid Search` & `Paid Social` cohorts generate **44.7% (890 accounts)** of permanently dead non-buyers; and `VIP` cohorts exhibit a **43.9% structural churn rate**. | Replaces blanket storewide changes with cohort-specific interventions—such as **Guest Checkout A/B testing** for New/Paid cohorts and reallocating ad spend toward conversion-optimized objectives. | 
| **Funnel Analysis** | Quantify leakage across the user journey and pinpoint the exact screen where purchase intent evaporates. | Mapped 25,000 sessions into a 6-stage sequence (`Session Start` → `Page View` → `View Item` → `Add to Cart` → `Begin Checkout` → `Purchase`); engineered stage-to-stage and cumulative drop-off DAX measures. | Primary leakage walls occur at: (1) **Add to Cart → Begin Checkout (50.17% overall / ~77%–80% for Lost Paid Cohorts)** and (2) **View Item → Add to Cart (37.46% leakage)**, plus a hidden **2.39% broken first-order rate** post-purchase click. | Directs engineering and UX **A/B testing** toward high-friction screens (forced registration walls, upfront shipping calculators, and payment validation) to recover lost sales. | 
| **Dual-Layer Churn Analysis** | Distinguish between customers who stopped buying versus those who stopped engaging with the platform altogether. | Formulated a 2D retention matrix crossing **Purchase Churn** (SQL-calculated days since last order vs. median cycle benchmark) with **Activity Churn** (DAX recency of last web session event). | While **87.49% of users are in an unsafe purchasing state**, crossing with live activity proves **49.77% (4,977 users) are Active Browsers**—where **61% (3,047 users) are Active Non-Buyers** and **25% of Churned Buyers are still active on-site**, while isolating **2,897 permanently dead accounts**. | Unlocks a projected **+\$5.52M (+20.4% revenue lift)** by converting 30% of Active Non-Buyers, saves **31.5% in wasted retargeting spend**, and prioritizes low-CAC win-back for the 25% active churned buyers. | 
| **Customer Segmentation** | Avoid generic marketing by treating non-buyers, active buyers, and high-LTV VIPs as distinct populations. | Segmented users in SQL/DAX across two axes: Lifecycle Status (`Never Bought`, `Active`, `At-Risk`, `Churned`) and Spending Quartile Tiers (`Budget`, `Mid-Tier`, `VIP`). | Exposed a "Zero-Loyalty Ecosystem" (~44% uniform churn): **65.9% of VIPs (608 top buyers)** and **66.8% of Mid-Tier buyers (1,233 users)** are currently either `Churned` or `At-Risk`, threatening two-thirds of historical revenue. | Enables targeted lifecycle email sequences, dynamic free-shipping thresholds by tier, and urgent VIP concierge win-back workflows. | 
| **Behavioral Analysis** | Understand in-session shopper friction, basket-building habits, and hesitation before an order decision. | Sequenced session events by timestamp using SQL Window Functions; analyzed basket item counts (`Single-Item` vs. `Multi-Item` carts) and dwell time between `Add to Cart` and `Begin Checkout`. | Revealed that `Entry-Level` and `Core` paid cohorts add items to cart at healthy rates (~53%–55% retention) but abandon at `Begin Checkout` (**76.92%–79.35%**) and `Purchase` (**81.58% Entry-Level drop-off**) due to shipping sticker shock and checkout friction. | Informs psychological checkout nudges and **A/B experiments**, such as dynamic "Add \$X for Free Shipping" progress bars on the Cart page and BNPL split-payment options. | 
| **Comparative / Diagnostic Analysis** | Empirically test whether paid traffic conversion barriers stem from `Premium` catalog pricing or systemic checkout friction. | Engineered DAX trace (`Lost_NonBuyers_Paid_Last_Assortment`) slicing dead `Paid Search` & `Paid Social` users across Product Price Tiers (`Core`, `Entry-Level`, `Premium`) and Product Categories. | **Debunked the "Premium Price Shock" myth:** Most lost paid users dropped off after viewing **Core (379 users)** and **Entry-Level (212 users)** assortments, versus only **195 in Premium**, with identical ~77%–80% `Begin Checkout` collapse across all three tiers. | Eliminates marketing guesswork; shifts focus from blaming catalog pricing to running **Checkout UX A/B Tests** and transitioning Paid Social from low-intent link-click volume to Purchase-optimized targeting. | 
| **Order Lifecycle Analysis** | Evaluate first-purchase acquisition friction separately from repeat buyer loyalty velocity. | Tagged transactions in `vw_fact_sales_enriched.sql` (`order_lifecycle_tag`) into: `Immediate First Purchase`, `Delayed First Purchase` (multi-session consideration), and `Repeat Purchase` by comparing `session_start` to `first_completed_date`. | Initial transactions are predominantly **Delayed First Purchases** requiring multi-session comparisons and facing a **2.39% failure rate**, whereas **Repeat Purchases convert at a significantly faster velocity and higher AOV**. | Proves that breaking first-order friction is the ultimate LTV catalyst; mandates 48-hour consideration retargeting and immediate service recovery for failed first orders. | 

## 4. Deep-Dive Analytical Findings: How Cohort Segmentation Exposed the Leakage

Every insight generated by Cartiva is structured into confirmed quantitative evidence, data-backed hypotheses, and commercial actionability:

### Finding 1: The Checkout Wall & The 2.39% Broken First-Order Anomaly

- **The Observation:** Over half of high-intent carts are abandoned right before payment, and first-order transactions require significantly longer multi-session consideration (`Delayed First Purchase`)—compounded by a hidden technical fulfillment failure.

- **The Cohort Evidence:**

  * Overall **Add to Cart → Begin Checkout leakage is 50.17%** (50.96% session-adjusted), but spikes to a staggering **78.89% within the `New Visitor` cohort**.

  * Slicing `vw_fact_sales_enriched` by `order_lifecycle_tag` proves that while first-time buyers hesitate across multiple sessions, once they complete Order #1, their **Repeat Purchases happen at a much faster velocity and generate a higher Average Order Value (AOV)**.

  * Isolating the **`1,990 Dead Non-Buyer` cohort** (`Never Bought × Activity Churned`) revealed that **2.39% actually clicked `Purchase`**, meaning their first orders failed technically, were cancelled, or returned—causing them to abandon Cartiva forever.

- **Commercial Action ("The Pill"):** Deploy an automated **Service Recovery protocol** (apology voucher + direct cart restoration link) for the **2.39% failed first-order prospects** so technical glitches never permanently burn acquired CAC, while streamlining first-order checkout via **Guest Checkout** and **BNPL** options.

### Finding 2: Debunking the "Premium Price Shock" Myth & The Paid Traffic Checkout Wall

- **The Observation:** Marketing initially assumed that the **890 permanently dead accounts** acquired via `Paid Search` (489 users) and `Paid Social` (401 users) bounced because ads routed them to expensive `Premium Assortment` items. Empirical DAX tracking (`Lost_NonBuyers_Paid_Last_Assortment`) proved this hypothesis **completely false**.

- **The Cohort Evidence:**

  * Tracing the exact last product price tier viewed by lost paid users revealed that abandonment is highest in mass-market tiers: **Core Assortment (379 lost users)** and **Entry-Level Assortment (212 lost users)**, while **Premium Assortment accounted for the lowest volume (195 lost users)**.

  * Cross-tier funnel slicing proves **the products and prices are not the problem**: `View Item` drop-off is consistently low (**15.97% Core**, **16.35% Entry-Level**, **18.18% Premium**) and `Add to Cart` drop-off (**45.83% Core**, **47.13% Entry-Level**, **45.10% Premium**) actually **outperforms the general site benchmark**. Over half of these lost paid users liked the item enough to load their cart!

  * The real collapse triggers exclusively at **`Begin Checkout`**, exploding to **76.92% in Core** (89.50% cumulative), **79.35% in Entry-Level** (90.87% cumulative), and **79.76% in Premium** (90.91% cumulative)—exceeding the site-wide benchmark bar by ~25 percentage points—followed by a massive **81.58% `Purchase` stage failure in Entry-Level** (vs. 73.33% Core and 58.82% Premium).

- **Data-Backed Hypotheses (Why Paid Cohorts Abandon at Checkout):**

  * **Hypothesis 1 — Hidden Costs & Shipping Sticker Shock:** Budget and Core shoppers approve of the item price (`Add to Cart`), but encounter unexpected flat-rate shipping fees or taxes at `Begin Checkout`/`Purchase` that disproportionately inflate the total cost of an `Entry-Level` item (explaining the **81.58% Entry-Level purchase drop-off**).

  * **Hypothesis 2 — Forced Account Registration Friction:** Impulse shoppers arriving from `Paid Social` hit a mandatory account creation and email verification wall at `Begin Checkout`, causing ~80% to bail rather than complete a lengthy form for a basic item.

  * **Hypothesis 3 — Low-Intent "Price Discovery" Clickers:** `Paid Social` campaigns optimized for cheap link clicks attract window-shoppers who click `Add to Cart` and `Begin Checkout` purely to discover the final shipping-adjusted price, possessing zero true purchase intent.

- **Commercial Action & A/B Testing Roadmap ("The Pill"):**
  1. **A/B Test 1 (Friction Reduction — Guest Checkout):** Run a controlled experiment comparing the current "Forced Registration" flow against a **1-Click Guest Checkout** option to compress the ~80% `Begin Checkout` drop-off among Paid Social/Search traffic.
  2. **A/B Test 2 (Sticker Shock Mitigation — Transparent Shipping):** Test displaying a dynamic **"Free Shipping on orders over \$X"** progress bar and upfront shipping calculator directly inside the `Add to Cart` drawer to pre-qualify buyers and curb the 81.58% Entry-Level checkout failure.
  3. **Ad Targeting & PDP Re-Alignment:** Transition `Paid Social` campaigns from top-of-funnel "Traffic/Link Clicks" to strict **Conversion/Purchase-optimized** objectives, while upgrading high-hesitation category PDPs (**Furniture 48.73% drop-off** & **Beauty 47.73% drop-off**) with trust badges and photo reviews.

### Finding 3: The Dual-Churn Matrix, The +\$5.52M Hidden Gem & Structural VIP Attrition

- **The Observation:** While **87.49% of the total customer base** sits in an unsafe purchasing zone, crossing transactional status with live web activity uncovers a massive, zero-CAC revenue goldmine alongside an urgent VIP loyalty crisis.

- **The Cohort Evidence:**

  * **The +\$5.52M Hidden Gem (`Active Browsers × Never Bought`):** The Dual-Churn Matrix proves that **49.77% (4,977 users)** of the entire database are **Active Browsers**. Crucially, **61% of these active users (3,047 profiles) are `Never Bought` window-shoppers** whose acquisition cost is already sunk. Converting just **30%** of this active cohort at the baseline **\$6,040 AOV** yields a **+20.4% surge in total company revenue**:
    $$\text{Projected Revenue Lift} = (3,047 \text{ Active Non-Buyers} \times 30\%) \times \$6,040 \text{ AOV} = 914 \text{ New Buyers} \times \$6,040 = \mathbf{+\$5,520,560}$$

  * **The Low-Hanging Fruit (`25% Active Churned`):** Exactly **25% of historically `Churned` buyers are still `Active Browsers`** (408 active past buyers overall) who regularly visit the site. Re-activating these brand-familiar past buyers requires a fraction of cold acquisition CAC.

  * **Structural VIP Churn ("Zero-Loyalty Ecosystem"):** Crossing **Spending Tiers × Churn Status** reveals that Cartiva operates without retention differentiation—churn is flat at **~44% across all brackets**. Specifically, **VIPs churn at 43.9%**, with combined Churned and At-Risk VIPs reaching **65.9% (608 VIPs)**, mirrored by **66.8% in the Mid-Tier (1,233 users)**—putting **two-thirds of historical baseline revenue** in immediate jeopardy.

- **Commercial Action ("The Pill"):** 
  1. **Capture the +\$5.52M Gem:** Trigger automated in-session first-order incentives (e.g., *Free Express Shipping + First-Order Guarantee*) for the **3,047 Active Non-Buyers**.
  2. **Low-CAC Win-Back & Ad Savings:** Suppress the **2,897 permanently dead accounts** from paid retargeting to **save 31.5% in ad spend**, reinvesting those funds into personalized "Welcome Back" credits for the **25% Active Churned** cohort.
  3. **VIP Loyalty Program:** Halt the 65.9% VIP attrition by launching a tiered **VIP Concierge & Loyalty Program** (automatic free shipping, priority inventory access, and milestone rewards) for top-tier and Mid-Tier buyers.

## 5. Project Implementation Roadmap

To provide full engineering transparency on current deliverables versus upcoming milestones:

```
├── [COMPLETED / PRODUCTION-READY]
│   ├── Modular Python ETL pipeline with data standardization & schema validation
│   ├── Star-Schema Data Warehouse tables deployed in MySQL 8.0
│   ├── Enriched analytical SQL views (User lifecycle, 6-stage Funnel sequencing, Sales lifecycle)
│   ├── Enterprise Power BI Project (.pbip) with TMDL semantic model definitions
│   ├── Core & Advanced DAX measure library (Dual-Churn matrix, Stage leakage %, Lost Paid Assortment trace)
│   ├── Executive Overview Dashboard (KPIs, Monthly Trends, Funnel Drop-offs, Churn Split, Traffic Mix)
│   ├── Page 2: Customers & Cohort Retention Dashboard (Dual-Churn matrix, VIP Structural Churn, CAC bleed)
│   └── Executive Documentation PDFs (Strategic Blueprint & Important Findings Executive Brief)
│
├── [IN PROGRESS — ACTIVE POWER BI BUILD]
│   └── Page 3: Funnel Diagnostics Dashboard (Cohort-sliced drop-offs by Visitor Type, Category & Price Tier)
│
└── [PLANNED — PHASE 2 ENHANCEMENTS]
    ├── Time-Based Monthly Cohort Retention Heatmap (12-month repeat purchase decay grid)
    └── A/B Test Statistical Calculator for Guest Checkout & Free-Shipping threshold experiments
```

## 6. Data Architecture & Star Schema Modeling

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

- **Granularity Isolation:** `Fact_Events` captures clickstream progression (`view_item`, `add_to_cart`, `begin_checkout`) at the **session-timestamp grain** across 25,000 sessions. `Fact_Sales` records completed monetary transactions at the **order-item line grain**.

- **Query Performance & DAX Accuracy:** Merging clickstream logs with order financials into a single flat table causes severe row inflation and distorts conversion denominators. Isolating them allows DAX measures to seamlessly cross-filter behavioral cohorts against actual revenue yield via shared dimensions (`Dim_Customers`, `Dim_Sessions`, `Dim_Products`).

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

- **Extraction (`data_extraction.py`):** Streams raw operational tables from MySQL using pooled `SQLAlchemy` connections.

- **Transformation & Cleaning (`Data_cleaning.py`):**

  * Normalizes fragmented UTM/traffic tags into standardized acquisition cohorts (e.g., consolidating raw social referrals into `Paid Social`).

  * Resolves missing timestamps, standardizes date/time partitions, imputes missing catalog categories, and validates pricing integrity.

- **Warehouse Loading (`data_loading.py`):** Upserts cleaned dimension and fact tables into the MySQL analytics schema with strict referential integrity.

- **Orchestration (`main.py`):** Single-command runner that executes the end-to-end Extract-Transform-Load sequence.

## 9. How to Reproduce & Run the Project

### Prerequisites

- **Python 3.10+**

- **MySQL Server 8.0+**

- **Power BI Desktop** (with `.pbip` Power BI Project developer mode enabled)

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
├── Cartiva.Report/                  # Power BI visual layout, custom JSON themes & page definitions
├── Cartiva.SemanticModel/           # Power BI semantic data model & DAX library (TMDL format)
├── Dashboard Designs/               # UI screenshots, layout grids, and wireframes
│   ├── Cartiva_Overview_Dashboard.jpg
│   ├── Cartiva_Overview_Layout.jpg
│   ├── Cartiva_Overview_Wireframe.png
│   └── Cartiva_Customer_Intelligence.png
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