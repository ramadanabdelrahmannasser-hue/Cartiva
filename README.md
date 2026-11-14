# Cartiva — E-Commerce Product, Cohort & Funnel Analytics

![Cartiva Overview Dashboard](Dashboard%20Designs/Cartiva_Overview_Dashboard.jpg)

> **Project Status: Active Development (Phase 1 Completed)**
>
> The **Executive Overview Dashboard**, SQL semantic layer, and Python ETL pipeline are fully deployed and operational. Deep-dive diagnostic views (**Customers & Cohort Retention** and **Funnel Diagnostics**) are actively being finalized in Power BI.

---

## Executive Story Brief: The Leaky Bucket Paradox

**Cartiva** had no problem attracting attention. Thousands of visitors flooded the platform across **25,000+ browsing sessions**, generating **$27M in revenue** and making the business look like a thriving e-commerce success on the surface. 

Yet behind the scenes, the platform was bleeding at both ends of the customer journey:
* **The Visitors Who Never Buy:** Massive waves of shoppers actively browsed product pages and even loaded their carts, only to vanish right before completing their order—leaving **56.58% of all registered users with zero purchases**.
* **The Buyers Who Never Return:** Worse still, converting a visitor wasn't enough. Even the customers who completed a purchase—including top-spending **VIPs**—were quietly walking away after their orders, churning at nearly **44%** and never coming back.

Leadership didn't need another dashboard showing total sales; they needed to know **why shoppers were abandoning the funnel** and **why buyers weren't sticking around**. By engineering an end-to-end analytics pipeline (`Python ETL` → `MySQL Window Functions` → `Power BI Star Schema`) and grouping users into **behavioral, acquisition, and spending cohorts**, this project diagnoses the exact friction points causing funnel leakage and exposes the retention gaps draining customer lifetime value.

---

## 1. The Business Story: Why "\$27M in Revenue" Was Hiding a Silent Crisis

On paper, **Cartiva** looked like an e-commerce success story. Top-line reports showed **\$27M in total revenue** across **4,000+ completed orders**, an impressive **\$6.04K Average Order Value (AOV)**, and a **36.88% Buyer Conversion Rate**, with monthly revenue surging exponentially to **\$12.5M in June**.

However, beneath this rapid top-line growth, unit economics were quietly deteriorating:

1. **The Conversion Black Hole:** Marketing was pouring budget into traffic acquisition across **25,000+ sessions**, yet **56.58% of registered users (5,658 profiles) had never completed a single purchase**.

2. **Invisible Funnel Friction:** Leadership knew visitors were leaving, but lacked visibility into *where* intent evaporated across the 6-stage shopping journey (`Session Start` → `Purchase`)—or *which specific user cohorts* were hitting walls.

3. **The "Zero-Loyalty" Trap:** Standard reporting lumped all inactive users together. The business could not distinguish between a permanently dead account and an active window-shopper, nor did it realize that its highest-spending VIPs were quietly abandoning the platform at the exact same rate as budget shoppers.

### Mission Objective

Instead of building another static sales tracker, **Cartiva** was engineered as an end-to-end product analytics and behavioral diagnostic system. By combining a **Python ETL pipeline**, **MySQL Window Functions**, and a **TMDL-structured Power BI Semantic Model**, this project groups users into actionable **behavioral, acquisition, and spending cohorts**—using those cohorts to isolate the exact root causes of funnel leakage, recover wasted ad spend, and halt structural customer churn.

## 2. Dashboard Architecture & UI Previews

Designed around *Storytelling with Data* principles, the UI eliminates visual clutter, enforces a cohesive custom color hierarchy (slate navy, sage olive gradients, and high-alert coral red reserved strictly for critical drop-offs), and guides executive attention directly to commercial bottlenecks.

### Overview UI Layout & Wireframe Architecture

The report is architected as a modular 3-page SaaS application with a persistent left navigation rail and standardized analytical containers:

![Cartiva Overview Layout](Dashboard%20Designs/Cartiva_Overview_Layout.jpg)

| Report Page | Status | Primary Commercial & Product Questions Answered | 
| ----- | ----- | ----- | 
| **1. Overview** | **Completed** | How are we performing against macro KPIs? Where is the steepest funnel drop-off occurring? What is the true health of our customer base when crossing purchase history with live browsing activity? | 
| **2. Customers** | **In Progress** | How do our user cohorts behave across the Dual-Churn Matrix (`Purchase Churn × Activity Churn`)? How much historical LTV is at risk due to Structural VIP Churn? Which acquisition channels generate permanently dead accounts? | 
| **3. Funnel** | **In Progress** | How do specific user cohorts (New vs. Returning, Price Tiers, and Traffic Channels) experience funnel leakage? Which product categories suffer the worst View-to-Cart trust deficits? Why are first-time orders failing after checkout? | 

## 3. Analytical Methodologies & Cohort-Driven Diagnostics

Cartiva moves beyond surface-level reporting by applying eight specialized analytical frameworks—using **Cohort Grouping** as the primary lens to diagnose funnel leakage and retention decay:

| Analysis Type | Why It Was Used (Why) | Implementation Details (How) | Key Findings / Indicators (Findings) | Commercial Actionability (Business Value) | 
| ----- | ----- | ----- | ----- | ----- | 
| **Descriptive Analysis** | Establish an executive commercial baseline before investigating causal mechanics. | Synthesized top-level KPI cards (Revenue, Orders, AOV, Buyer Conversion %) alongside monthly trend lines and traffic distributions in Power BI. | Revenue reached **\$27M** across **4K orders** with a **\$6.04K AOV** and **36.88% Buyer Conversion %**, demonstrating rapid revenue acceleration peaking in June (**\$12.5M**). | Aligns executive leadership on baseline commercial velocity and highlights whether growth is driven by order volume or basket size. | 
| **Cohort Analysis (Behavioral & Acquisition Cohorts)** | Group users into distinct shared-trait cohorts to uncover *who* is experiencing funnel leakage and *why* retention decays post-acquisition. | Segmented the 10,000-user base into **Onboarding Cohorts** (`New Visitors` vs. `Returning`), **Acquisition Channel Cohorts** (`Paid Search`, `Paid Social`, `Organic`, `Referral`), **Spending Tiers** (`Budget`, `Mid-Tier`, `VIP`), and **Recency Cohorts**. Cross-tabulated each cohort against stage-by-stage funnel drop-offs. | Cohort isolation proved that funnel leakage is not uniform: `New Visitor` cohorts suffer a **78.89% Cart-to-Checkout drop-off** (vs. 50.17% overall); `Paid Search` & `Paid Social` cohorts generate **44.7% (890 accounts)** of permanently dead non-buyers; and `VIP` cohorts exhibit a **43.9% structural churn rate**. | Replaces blanket storewide changes with cohort-specific interventions—such as guest checkout for New Visitor cohorts and reallocating ad spend toward high-retention Referral and Paid Social cohorts. | 
| **Funnel Analysis** | Quantify leakage across the user journey and pinpoint the exact screen where purchase intent evaporates. | Mapped 25,000 sessions into a 6-stage sequence (`Session Start` → `Page View` → `View Item` → `Add to Cart` → `Begin Checkout` → `Purchase`); engineered stage-to-stage and cumulative drop-off DAX measures. | Primary leakage walls occur at: (1) **Add to Cart → Begin Checkout (50.17% user drop-off / 50.96% session drop-off)** and (2) **View Item → Add to Cart (37.46% leakage)**, plus a hidden **2.39% broken first-order rate** post-purchase click. | Directs engineering and UX optimization toward high-friction screens (cart review, shipping fee calculation, and checkout validation) to immediately recover lost sales. | 
| **Dual-Layer Churn Analysis** | Distinguish between customers who stopped buying versus those who stopped engaging with the platform altogether. | Formulated a 2D retention matrix crossing **Purchase Churn** (SQL-calculated days since last order vs. median cycle benchmark) with **Activity Churn** (DAX recency of last web session event). | While **56.58% Never Bought** and **19.07% Churned** transactionally, crossing with live activity proves **49.77% (4,977 users) are Active Browsers**—uncovering **3,047 Active Non-Buyers** and **408 Active Past Buyers**, while isolating **2,897 permanently dead accounts**. | Saves **31.5% in wasted retargeting ad spend** by suppressing dead accounts, while triggering immediate in-session conversion nudges for the 3,047 active window-shoppers. | 
| **Customer Segmentation** | Avoid generic marketing by treating non-buyers, active buyers, and high-LTV VIPs as distinct populations. | Segmented users in SQL/DAX across two axes: Lifecycle Status (`Never Bought`, `Active`, `At-Risk`, `Churned`) and Spending Quartile Tiers (`Budget`, `Mid-Tier`, `VIP`). | Exposed a "Zero-Loyalty Ecosystem": **65.9% of VIPs (608 top buyers)** and **66.8% of Mid-Tier buyers (1,233 users)** are currently either `Churned` or `At-Risk`, threatening two-thirds of historical revenue. | Enables targeted lifecycle email sequences, dynamic free-shipping thresholds by tier, and urgent VIP concierge win-back workflows. | 
| **Behavioral Analysis** | Understand in-session shopper friction, basket-building habits, and hesitation before an order decision. | Sequenced session events by timestamp using SQL Window Functions; analyzed basket item counts (`Single-Item` vs. `Multi-Item` carts) and dwell time between `Add to Cart` and `Begin Checkout`. | Revealed that `Budget` cohorts abandon single-item carts due to flat-rate shipping shock, while `Mid-Tier` cohorts abandon multi-item carts (3+ items) due to cumulative bill shock at checkout. | Informs psychological checkout nudges, such as dynamic "Add \$X for Free Shipping" progress bars and Buy-Now-Pay-Later (BNPL) split-payment options. | 
| **Comparative / Diagnostic Analysis** | Test whether conversion barriers stem from traffic source mismatch, device UX, or catalog pricing. | Dimensional cuts slicing funnel drop-off rates across Traffic Channels (`Organic`, `Paid Search`, `Paid Social`, `Email`, `Direct`, `Referral`), Product Categories, and Price Tiers (`Budget`, `Mid`, `Premium`). | **Furniture (48.73% drop-off)** and **Beauty (47.73% drop-off)** drive View-to-Cart leakage. Meanwhile, `Paid Search` and `Email` cohorts fail heavily when routed to `Premium` products, whereas `Paid Social` converts high-ticket items effectively. | Eliminates marketing guesswork; guides performance teams to realign Paid Search ad copy with budget/mid-tier landing pages and shift Premium catalog spend to Paid Social. | 
| **Order Lifecycle Analysis** | Evaluate first-purchase acquisition friction separately from repeat buyer loyalty velocity. | Tagged transactions in `vw_fact_sales_enriched.sql` into: `Immediate First Purchase` (same-session order), `Delayed First Purchase` (multi-session consideration), and `Repeat Purchase`. | Initial transactions require multiple evaluation sessions and face a **2.39% cancellation/failure rate** among lost prospects, while repeat purchases exhibit higher velocity when first-order fulfillment succeeds. | Establishes optimal retargeting windows (48-hour consideration sequences) and mandates automated customer support intervention for failed first orders. | 

## 4. Deep-Dive Analytical Findings: How Cohort Segmentation Exposed the Leakage

Every insight generated by Cartiva is structured into confirmed quantitative evidence, root-cause diagnosis, and commercial actionability:

### Finding 1: The Checkout Wall & The 2.39% Broken First-Order Anomaly

* **The Observation:** Over half of high-intent carts are abandoned right before payment, but cohort slicing reveals the problem is overwhelmingly concentrated among first-time visitors—compounded by a hidden fulfillment failure.

* **The Cohort Evidence:**

  * Overall **Add to Cart → Begin Checkout leakage is 50.17%** (50.96% session-adjusted), but spikes to a staggering **78.89% within the `New Visitor` cohort**.

  * Slicing by **Spending & Basket Cohorts** shows `Budget` users abandoning 1-item carts (shipping fee shock) and `Mid-Tier` users abandoning 3+ item carts (total bill shock).

  * Isolating the **`1,990 Dead Non-Buyer` cohort** (`Never Bought × Activity Churned`) revealed that **2.39% actually clicked `Purchase`**, meaning their first orders failed, were cancelled, or returned—causing them to abandon Cartiva forever.

* **Commercial Action ("The Pill"):** Replace forced account creation with **1-Click Guest Checkout** for New Visitors, introduce **BNPL (4 interest-free installments)** on carts over \$500, and deploy an automated VIP support recovery protocol whenever a first-time buyer's order fails or is cancelled.

### Finding 2: Category Trust Deficits & Paid Channel Cohort Mismatch

* **The Observation:** More than a third of product views fail to result in a cart addition (**37.46% View-to-Cart leakage**), driven by acute category hesitation and misaligned paid acquisition cohorts.

* **The Cohort Evidence:**

  * Slicing catalog views by **Product Category** exposes severe leakage in **Furniture (48.73% drop-off)** and **Beauty (47.73% drop-off)**, where shoppers require high visual reassurance and ingredient/dimension clarity before committing.

  * Crossing **Acquisition Channel Cohorts × Product Price Tiers** proves that **`Paid Search` and `Email` cohorts** suffer massive drop-offs when landing on `Premium` inventory, while **`Paid Social` cohorts** demonstrate strong conversion affinity for high-ticket `Premium` items.

* **Commercial Action ("The Pill"):** Upgrade Furniture and Beauty PDPs with 3D/AR room previews, verified buyer photo reviews, and bold "Free 30-Day Returns" badges. Reallocate `Premium` product ad budgets away from Paid Search and into Paid Social lookalike campaigns.

### Finding 3: The Dual-Churn Matrix, CAC Bleed & Structural VIP Attrition

* **The Observation:** Traditional churn metrics hide active commercial opportunities while masking a severe loyalty crisis among top-tier spenders.

* **The Cohort Evidence:**

  * **The Dual-Churn Matrix (`Purchase Churn × Activity Churn`):** Proves that **49.77% (4,977 users)** of the database are actively browsing the store. More importantly, **3,047 of the 5,658 "Never Bought" users are Active Browsers** currently on-site, and **408 Past Buyers (`Churned`/`At-Risk`)** have returned to window-shop.

  * **Paid CAC Bleed:** Tracing the acquisition source of the **1,990 permanently dead non-buyers** reveals that **Paid Search (489 users)** and **Paid Social (401 users)** are responsible for **44.7% of dead traffic**, whereas the **Referral cohort** produced only 92 dead accounts (highest retention quality).

  * **Structural VIP Churn:** Crossing **Spending Tiers × Churn Status** proves that **VIPs churn at 43.9%** (with **65.9% / 608 VIPs** either Churned or At-Risk), virtually identical to **Mid-Tier (43.8% churn / 66.8% at-risk)** and **Budget (44.8% churn)**.

* **Commercial Action ("The Pill"):** Immediately exclude the **2,897 permanently dead accounts** (`1,990 Never Bought` + `907 Churned/At-Risk` with zero activity) from paid retargeting to **save 31.5% in ad spend**. Reinvest those savings into automated "Welcome Back" checkout credits for the **408 active past buyers** and launch a tiered VIP Loyalty Program (free express shipping & priority access) to protect the top two-thirds of historical revenue.

## 5. Project Implementation Roadmap

To provide full engineering transparency on current deliverables versus upcoming milestones:

```
├── [COMPLETED / PRODUCTION-READY]
│   ├── Modular Python ETL pipeline with data standardization & schema validation
│   ├── Star-Schema Data Warehouse tables deployed in MySQL 8.0
│   ├── Enriched analytical SQL views (User lifecycle, 6-stage Funnel sequencing, Sales lifecycle)
│   ├── Enterprise Power BI Project (.pbip) with TMDL semantic model definitions
│   ├── Core & Advanced DAX measure library (Dual-Churn matrix, Stage leakage %, AOV, Conversion)
│   ├── Executive Overview Dashboard (KPIs, Monthly Trends, Funnel Drop-offs, Churn Split, Traffic Mix)
│   └── Comprehensive Strategic Blueprint PDF (Full cohort matrices, root-cause diagnostics & action plans)
│
├── [IN PROGRESS — ACTIVE POWER BI BUILD]
│   ├── Page 2: Customers & Cohort Retention Dashboard (Dual-Churn matrix, VIP Structural Churn, CAC bleed)
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
│ Dim_Customers  ├───────►  Fact_Events   │        │   Fact_Sales   │◄───────┐
└───────┬────────┘ (1:N) └────────────────┘        └────────────────┘ (N:1)  │
        │ (1:N)                                                              │
        └────────────────────────────────────────────────────────────┐       │
                                                                     │       │
                                                            ┌────────┴───────┴┐
                                                            │  Dim_Products   │
                                                            └─────────────────┘

```

### Why Separate `Fact_Events` and `Fact_Sales`?

* **Granularity Isolation:** `Fact_Events` captures clickstream progression (`view_item`, `add_to_cart`, `begin_checkout`) at the **session-timestamp grain** across 25,000 sessions. `Fact_Sales` records completed monetary transactions at the **order-item line grain**.

* **Query Performance & DAX Accuracy:** Merging clickstream logs with order financials into a single flat table causes severe row inflation and distorts conversion denominators. Isolating them allows DAX measures to seamlessly cross-filter behavioral cohorts against actual revenue yield via shared dimensions (`Dim_Customers`, `Dim_Sessions`, `Dim_Products`).

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

   * Evaluates transaction timestamps relative to user onboarding and session history.

   * Segments orders into `Immediate First Purchase` (single-session conversion), `Delayed First Purchase` (multi-session consideration cohort), and `Repeat Purchase`.

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
├── Cartiva.Report/                  # Power BI visual layout, custom JSON themes & page definitions
├── Cartiva.SemanticModel/           # Power BI semantic data model & DAX library (TMDL format)
├── Dashboard Designs/               # UI screenshots, layout grids, and wireframes
│   ├── Cartiva_Overview_Dashboard.jpg
│   ├── Cartiva_Overview_Layout.jpg
│   └── Cartiva_Overview_Wireframe.png
├── Documentation/                   # Deep-dive executive blueprints & strategic documentation
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
