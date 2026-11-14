# Cartiva - E-commerce Product Analytics

![Cartiva Overview Dashboard](Dashboard%20Designs/Cartiva_Overview_Dashboard.jpg)

> **Project Status: In Progress**  
> The **Overview Dashboard** is fully completed and operational. Supporting analytical pages (deep-dive Funnel Analysis, Customer Health & Cohort retention, and Assortment/Channel diagnostics) are currently in active development.

---

## 1. Project Overview & Business Problem

### The Core Business Challenge
In modern e-commerce operations, generating web traffic is costly, yet high top-of-funnel traffic rarely translates directly into bottom-line profitability. **Cartiva** addresses a critical commercial issue: **a large volume of visitors actively browse product catalogs, but a substantial percentage drop off before completing their purchase.**

While top-level revenue metrics might appear healthy on the surface, leadership lacks visibility into:
1. **Funnel Leakage & Abandonment:** Exactly where potential buyers drop out along the 6-stage journey from landing to transaction.
2. **Traffic Quality vs. Assortment Mismatch:** Whether paid customer acquisition channels are attracting visitors whose price sensitivity aligns with the inventory.
3. **Retention & Customer Health:** Identifying which customers are slipping into churn or remaining persistent non-buyers despite repetitive browsing sessions.

### Primary Objective
The core mission of Cartiva is to **diagnose the root causes of conversion drop-offs across the funnel and pinpoint high-friction touchpoints.** Secondary supporting analytical objectives evaluate customer retention, lifecycle velocity, and post-acquisition engagement to maximize Customer Lifetime Value (LTV).

---

## 2. Dashboard Previews

### Completed: Executive Overview Dashboard
The Executive Overview serves as the command center for commercial performance, high-level leakage diagnosis, traffic mix, and customer health monitoring.

![Cartiva Overview Dashboard](Dashboard%20Designs/Cartiva_Overview_Dashboard.jpg)

### Overview UI Layout & Structure
The dashboard was wireframed and designed with a dedicated navigation structure and purposeful analytical grouping.

![Cartiva Overview Layout](Dashboard%20Designs/Cartiva_Overview_Layout.jpg)

---

## 3. Analytical Methodologies

Cartiva goes beyond reporting aggregate metrics by applying specialized analytical frameworks tailored to specific commercial questions:

| Analysis Type | Why It Was Used (Why) | Implementation Details (How) | Key Findings / Indicators (Findings) | Commercial Actionability (Business Value) |
| :--- | :--- | :--- | :--- | :--- |
| **Descriptive Analysis** | Establish an executive commercial baseline before investigating causal mechanics. | Synthesized top-level KPI cards (Revenue, Orders, AOV, Conversion Rate) alongside monthly trend lines and traffic distributions in Power BI. | Revenue reached \$27M across 4K orders with a \$6.04K AOV and 36.88% Buyer Conversion %, demonstrating exponential revenue growth peaking in June (\$12.5M). | Aligns executive leadership on baseline health and highlights whether growth is driven by volume or basket size. |
| **Funnel Analysis** | Quantify leakage across the user journey and pinpoint where intent evaporates. | Mapped event logs into a 6-stage sequence (`Session Start` → `Page View` → `View Item` → `Add to Cart` → `Begin Checkout` → `Purchase`); calculated stage-to-stage and cumulative drop-off DAX measures. | Top drop-offs occur at: (1) **Add to Cart → Begin Checkout (50.17% leakage)** and (2) **View Item → Add to Cart (37.46% leakage)**. | Directs engineering and UX optimization toward high-friction screens (cart review and checkout barriers) to immediately recover lost sales. |
| **Churn Analysis** | Distinguish between customers who stopped buying versus those who stopped engaging altogether. | Formulated dual tracking dimensions: **Purchase Churn** (SQL-calculated days since last order vs. median benchmark) vs. **Activity Churn** (DAX recency of last session event). | Customer base distribution reveals: **Never Bought (56.58%)**, **Churned (19.07%)**, **Active (15.12%)**, and **At-Risk (9.24%)**. | Prevents wasting remarketing ad spend on permanently inactive visitors and triggers automated win-back workflows for high-value "At-Risk" buyers. |
| **Customer Segmentation** | Avoid generic communication by treating buyers and non-buyers as distinct populations. | Segmented users in SQL/DAX across two axes: Lifecycle Status (`Never Bought`, `Active`, `At-Risk`, `Churned`) and Spending Quartile Tiers (`Low`, `Medium`, `High`, `VIP`). | Over 56% of users registered in the database have never placed an order, representing a massive untransacted audience pool. | Enables targeted lifecycle email sequences, first-time buyer welcome incentives, and VIP retention programs. |
| **Behavioral Analysis** | Understand in-session shopper friction and hesitation before an order decision. | Event sequencing by session timestamp in SQL window functions; DAX duration tracking (time elapsed between `Add to Cart` and `Begin Checkout`). | Significant dwell times and session abandonments occur specifically between cart additions and checkout initiation. | Informs checkout redesigns, such as one-click checkout, guest checkout options, and proactive cart abandonment exit-intent popups. |
| **Comparative / Diagnostic Analysis** | Test whether conversion barriers stem from traffic acquisition, device UX, or catalog pricing. | Dimensional cuts slicing drop-off rates by Traffic Channel (`Organic`, `Paid Search`, `Paid Social`, `Email`, `Direct`, `Referral`), Device Category, and Product Price Tiers. | Organic Search brings the largest volume (7.5K sessions), but Paid channels display elevated drop-offs when landing directly on premium inventory tiers. | Eliminates guesswork; guides marketing to realign campaign ad copy with price-appropriate landing pages. |
| **Order Lifecycle Analysis** | Evaluate first-purchase acquisition friction separately from repeat buyer loyalty. | Tagged transactions in `vw_fact_sales_enriched.sql` into: `Immediate First Purchase` (same-session order), `Delayed First Purchase` (multi-session consideration), and `Repeat Purchase`. | Initial transactions require multiple evaluation sessions, while repeat purchases exhibit significantly higher velocity and higher AOV. | Informs product retargeting windows (e.g., retargeting within 48 hours for consideration-phase visitors). |

> [!NOTE]
> **Cohort Analysis Status:** Cohort retention tracking (measuring month-by-month repeat purchase decay by initial acquisition cohort) is scheduled for the upcoming analytical phase and will be added once the validation data pipelines are completed.

---

## 4. Implemented vs. In-Progress vs. Planned Analysis

To provide full transparency on development status:

```text
├── [COMPLETED / IMPLEMENTED]
│   ├── Python ETL pipeline with data standardization & schema migrations
│   ├── Star-schema data warehouse tables in MySQL
│   ├── Enriched analytical SQL views (User lifecycle, Event funnel, Sales lifecycle)
│   ├── Robust Power BI semantic data model with TMDL definitions
│   ├── Core DAX measure library (Funnel leakage %, Churn benchmarks, AOV, Conversion)
│   └── Executive Overview Dashboard (KPIs, Monthly Trends, Funnel Drop-offs, Churn Split, Traffic Mix)
│
├── [IN PROGRESS]
│   ├── Dedicated Funnel Deep-Dive Report Page (stage-by-stage drop-off breakdown by device & category)
│   ├── Customer Health & Retention Deep-Dive (RFM segmentation matrix and activity vs. purchase churn grids)
│   └── Assortment & Channel Alignment View (Paid channel conversion by product price quartile)
│
└── [PLANNED]
    ├── Monthly Cohort Retention Grid (decay rate tracking across 12-month cohorts)
    ├── Automated Data Quality & Anomaly Detection pipeline in Python
    └── A/B Test Experimentation Framework for checkout flow modifications
```

---

## 5. Key Analytical Findings & Evidence Structure

Every finding generated by Cartiva is categorized into confirmed observations, analytical interpretations, and testable hypotheses:

### Finding 1: High-Intent Cart Abandonment
- **Observation:** More than half of visitors who demonstrate high intent by adding items to their cart drop out before starting checkout.
- **Evidence:** Overview Funnel metrics show **Add to Cart → Begin Checkout leakage at 50.17%**.
- **Interpretation:** Shoppers are experiencing unexpected friction at the cart review stage (e.g., unexpected shipping costs, forced account creation, or complex promo code validation).
- **Recommendation:** Implement transparent upfront pricing on product pages, offer guest checkout, and deploy automated email/SMS cart abandonment reminders within 1–2 hours.

### Finding 2: Catalog Evaluation Hesitation
- **Observation:** Over a third of shoppers viewing detailed item specifications fail to commit items to their cart.
- **Evidence:** Overview Funnel metrics confirm **View Item → Add to Cart leakage at 37.46%**.
- **Interpretation:** Product detail pages (PDPs) may lack critical purchase reassurance (social proof, customer reviews, clear sizing/dimensions, or return policy details).
- **Recommendation:** Enhance PDPs with customer ratings, high-resolution imagery, delivery timeframe guarantees, and urgency indicators for low-stock items.

### Finding 3: Heavy Non-Transacting User Base
- **Observation:** The majority of registered profiles in the database have zero completed transactions.
- **Evidence:** Customer Health breakdown identifies **56.58% Never Bought** vs. **15.12% Active** and **19.07% Churned**.
- **Interpretation:** Onboarding and initial engagement loops fail to convert first-time registrants into first-time buyers.
- **Recommendation:** Trigger an aggressive first-purchase discount workflow (e.g., 15% off first order) within 24 hours of account creation.

---

## 6. Power BI Dashboard Architecture

Rather than a static single-page report, Cartiva is built as an enterprise **Power BI Project (`.pbip`)** using **TMDL (Tabular Model Definition Language)** for source-controlled BI development:

| Page Name | Status | Primary Commercial Questions Answered |
| :--- | :--- | :--- |
| **1. Executive Overview** | **Completed** | How are we performing against commercial KPIs? Which funnel stage loses the most revenue? What is our customer health distribution? Which acquisition channels drive the most traffic? |
| **2. Funnel Diagnostics** | **In Progress** | Does funnel leakage vary by mobile vs. desktop? Which specific product categories suffer the steepest drop-offs? How long does it take a customer to transition from cart to checkout? |
| **3. Customer Health & Retention** | **In Progress** | How many high-value customers are in the "At-Risk" zone? What is the average inter-purchase interval? Are inactive users still browsing our catalog? |
| **4. Assortment & Acquisition Mix**| **In Progress** | Are high-cost Paid Search campaigns driving traffic to price-sensitive products? Which channel delivers the highest margin customers? |

---

## 7. Data Architecture & Data Modeling

Cartiva implements an analytical **Star Schema** designed to separate behavioral web interactions from financial transaction grains:

```text
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
                                                            │  Dim_products   │
                                                            └─────────────────┘
```

### Why Separate `Fact_Events` and `Fact_Sales`?
- **Granularity Isolation:** `Fact_Events` records web interaction events (clicks, views, cart additions) at the **millisecond session level** (high volume, low financial density). `Fact_Sales` records financial transactions at the **order-item line grain** (invoice-level tracking).
- **Performance & Scalability:** Combining event clicks with order financials into a single table causes massive row inflation and slows down analytical DAX queries.
- **Dimensional Role:** `Dim_Customers`, `Dim_Sessions`, and `Dim_products` provide unified filtering across both facts, allowing seamless cross-analysis between event behavior and monetary yield.

---

## 8. SQL Semantic Layer & Transformations

The database layer utilizes MySQL views to encapsulate complex business logic and window functions prior to BI ingestion:

1. **[`vw_dim_users_enriched.sql`](SQL/vw_dim_users_enriched.sql) — Customer Lifecycle & Benchmarks:**
   - Aggregates lifetime orders, historical spend (LTV), and days elapsed since last purchase.
   - Calculates a global **median inter-purchase cycle benchmark** across the entire customer base.
   - Dynamically segments customers into `Active`, `At-Risk`, `Churned`, or `Never Bought`.

2. **[`vw_fact_events_enriched.sql`](SQL/vw_fact_events_enriched.sql) — Event Funnel & Session Sequencing:**
   - Normalizes raw event types into standardized 6-stage funnel taxonomy.
   - Utilizes `ROW_NUMBER() OVER (PARTITION BY session_id ORDER BY event_timestamp)` to track exact in-session navigational paths and event sequence numbers.

3. **[`vw_fact_sales_enriched.sql`](SQL/vw_fact_sales_enriched.sql) — Transaction Lifecycle Classification:**
   - Evaluates order timing relative to user creation date.
   - Tags each transaction as `Immediate First Purchase`, `Delayed First Purchase`, or `Repeat Purchase`.

---

## 9. Python ETL Pipeline

The ETL pipeline is modularized into discrete responsibilities located in the [`Python/`](Python) directory:

```text
Operational DB  ──► [data_extraction.py] ──► [Data_cleaning.py] ──► [data_loading.py] ──► Analytics Warehouse
```

- **Extraction (`data_extraction.py`):** Efficiently reads raw tables from MySQL using SQLAlchemy connections.
- **Cleaning & Standardization (`Data_cleaning.py`):**
  - Standardizes irregular traffic source values (e.g., consolidating raw `Social` tags to `Paid Social`).
  - Cleans missing timestamps and splits date/time components for date-table linking.
  - Imputes missing product categories and validates numeric pricing constraints.
- **Loading (`data_loading.py`):** Upserts structured dimensions and fact tables into the analytics schema.
- **Pipeline Runner (`main.py`):** Automated orchestrator that executes the extract-clean-load cycle sequentially.
- **Standalone Utility (`import mysql.py`):** An isolated development script used to generate synthetic linked orders and purchase sessions for simulation. *(Note: Not executed by `main.py`).*

---

## 10. How to Run the Project

### Prerequisites
- Python 3.10+
- MySQL Server 8.0+
- Power BI Desktop (with Power BI Project `.pbip` preview feature enabled)

### Step 1: Clone Repository
```bash
git clone https://github.com/ramadanabdelrahmannasser-hue/Cartiva.git
cd Cartiva
```

### Step 2: Set Up Python Environment & Run ETL
```bash
pip install -r Python/requirements.txt
python Python/main.py
```
*(You will be prompted to enter your local MySQL credentials safely).*

### Step 3: Deploy SQL Analytical Views
Open your MySQL client and execute the SQL scripts in order:
```bash
mysql -u root -p warehouse_db < SQL/vw_dim_users_enriched.sql
mysql -u root -p warehouse_db < SQL/vw_fact_events_enriched.sql
mysql -u root -p warehouse_db < SQL/vw_fact_sales_enriched.sql
```

### Step 4: Open Power BI Project
Double-click `Cartiva.pbip` to launch Power BI Desktop. Refresh data to pull the latest enriched views from your local warehouse.

---

## 11. Repository Structure

```text
.
├── Cartiva.pbip                     # Power BI Project entry point
├── Cartiva.Report/                  # Power BI visual layout, themes & page definitions
├── Cartiva.SemanticModel/           # Power BI semantic data model (TMDL format)
├── Dashboard Designs/               # Screenshots and wireframe UI designs
│   ├── Cartiva_Overview_Dashboard.jpg
│   ├── Cartiva_Overview_Layout.jpg
│   └── Cartiva_Overview_Wireframe.png
├── Documentation/                   # Deep-dive business blueprints & documentation
│   ├── Cartiva_Project_Summary_and_Key_Insights.pdf
│   └── Nile_Express_Strategic_Funnel_and_Retention_Blueprint.pdf
├── Python/                          # Python ETL pipeline codebase
│   ├── main.py                      # Main pipeline execution entry point
│   ├── data_extraction.py           # Database extraction logic
│   ├── Data_cleaning.py             # Data transformation & normalization
│   ├── data_loading.py              # Warehouse load routines
│   ├── database.py                  # SQLAlchemy engine helper
│   ├── import mysql.py              # Standalone data generation utility
│   └── requirements.txt             # Python dependencies
└── SQL/                             # Enriched analytical SQL views
    ├── vw_dim_users_enriched.sql    # Customer lifecycle & benchmark metrics
    ├── vw_fact_events_enriched.sql  # Funnel stage mapping & event sequence
    └── vw_fact_sales_enriched.sql   # Order lifecycle classification
```
