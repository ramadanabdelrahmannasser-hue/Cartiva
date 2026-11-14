# Cartiva - E-commerce Product Analytics

> **Status: In Progress**  
> The Overview dashboard page is complete. The supporting analytical pages, validation work, and additional report pages are still under development.

Cartiva is an end-to-end e-commerce product analytics project that turns operational e-commerce data into a decision-ready Power BI model. It combines a Python ETL pipeline, MySQL views, and Power BI to investigate customer behaviour, funnel leakage, retention signals, and channel-to-assortment alignment.

For the fuller technical and findings narrative, see the [project summary and key insights](Documentation/Cartiva_Project_Summary_and_Key_Insights.pdf).

![Cartiva Overview wireframe](Dashboard%20Designs/Cartiva_Overview_Wireframe.png)

## Project overview

The project starts with operational `users`, `sessions`, `events`, `orders`, `order_items`, and `products` tables. Python standardises and loads them into an analytics warehouse. SQL then creates enriched views for customer lifecycle, funnel sequence, and order lifecycle analysis. Power BI imports those views into a star-like reporting model.

The completed Overview page brings together revenue, completed orders, average order value, buyer conversion, monthly performance, traffic-source mix, customer health, and the most important funnel drop-offs.

## Business problem

E-commerce teams need to understand more than sales totals: where intent is lost, whether acquisition sources bring an appropriate audience for the assortment, and which customers show signs of purchase or browsing inactivity. Cartiva is designed to make those questions traceable from event-level activity through to orders and customer lifecycle status.

## Objectives

- Build a repeatable pipeline from operational data to an analytical warehouse.
- Model the customer, session, product, event, and sales relationships needed for e-commerce analysis.
- Measure conversion through the six-stage journey: Session Start, Page View, View Item, Add to Cart, Begin Checkout, and Purchase.
- Segment customer purchase recency and browsing activity against a median-based benchmark.
- Surface evidence for acquisition, assortment, pricing, checkout, and retention decisions.

## Technology stack

- **Python:** pandas, SQLAlchemy, mysql-connector-python
- **Database:** MySQL
- **Transformation / semantic logic:** SQL views and DAX
- **BI:** Power BI Project (`.pbip`), semantic model in TMDL

## Data architecture and ETL workflow

```text
Operational source tables
  users | sessions | events | orders | order_items | products
                     |
              Python ETL
  extract -> standardise / derive -> load warehouse tables
                     |
              MySQL views
  customer lifecycle | event funnel sequence | order lifecycle
                     |
            Power BI semantic model
                     |
            Overview dashboard
```

The pipeline extracts all available source tables, standardises Social to Paid Social in acquisition and traffic fields, removes redundant medium fields, splits event and order timestamps into date/time, and creates item-grain sales records with `line_amount`. It loads `dim_sessions`, `dim_users`, `dim_products`, `fact_events`, and `fact_sales` to the warehouse.

## Data model

The reporting model centres on `Fact_Events` and `Fact_Sales`:

- `Dim_Customers` carries acquisition, customer value, completed-order, recency, and dynamic churn attributes.
- `Dim_Sessions` supplies traffic source and device context.
- `Dim_products` supplies category, price, cost, and quartile-derived price tiers.
- `Fact_Events` records event-level funnel activity and the sequence of events in a session.
- `Fact_Sales` is at item grain and includes order status, line amount, and first/repeat-purchase lifecycle tags.

Relationships connect facts to customers, sessions, and products; Power BI also contains role-specific local date tables for event, order, session, and customer milestone dates.

## Analytical methodologies

Cartiva is structured around business questions first, then selects the analytical method that can answer each question. The methods below are supported by the ETL logic, SQL views, semantic model, or completed Overview page. Reported historical values are labelled separately because the repository does not include raw data for independent recomputation.

| Analysis type | Why it was used | Where it was applied | What it revealed / can reveal | Business value |
| --- | --- | --- | --- | --- |
| **Descriptive analysis** | Establish a shared view of commercial performance before investigating causes. | Overview KPI cards and the monthly revenue/orders trend. | Revenue, completed orders, average order value, buyer conversion, sessions, and traffic distribution. The completed page makes changes in these core measures visible together. | Gives stakeholders a reliable starting point and highlights when deeper analysis is needed. |
| **Funnel analysis** | Identify where sessions fail to advance from interest to purchase. | Event enrichment assigns one of six ordered funnel stages; DAX calculates distinct-session conversion, stage leakage, and cumulative leakage. | The legacy blueprint reported 37.46% View Item -> Add to Cart leakage and 50.96% Add to Cart -> Begin Checkout leakage; those figures require rerunning against Cartiva data. | Focuses investigation and experiments on the stages with the greatest potential conversion impact. |
| **Behavioral analysis** | Distinguish what customers do inside a session from their eventual order outcome. | Event sequencing within session; cart-to-checkout elapsed-time measure; activity-churn calculation from last session. | The model can compare event sequence, elapsed cart-to-checkout time, and browsing recency with purchase behaviour. | Supports practical questions about hesitation, abandoned intent, and reactivation audiences. |
| **Customer segmentation** | Avoid treating buyers, non-buyers, and inactive customers as a single population. | SQL enrichment assigns purchase churn; DAX adds activity churn and customer spending tiers based on completed-order history and quartiles. | Segments include Active, At-Risk, Churned, Never Bought, and browsing-activity counterparts. The legacy blueprint reported 1,990 Never Bought x Activity Churned prospects and 1,641 permanently lost buyers, pending validation. | Enables targeted lifecycle, retention, and win-back decisions rather than generic outreach. |
| **Comparative / diagnostic analysis** | Test whether performance differs by customer or commerce context rather than assuming one cause. | Existing exploratory metadata cuts leakage by traffic source, device, product category, product price tier, spending tier, and channel x price tier. | The legacy blueprint reported higher View-to-Cart leakage in Furniture (48.73%) and Beauty (47.73%), and 37.81% for Paid Search on Premium. These are reported patterns, not independently recalculated Cartiva results. | Helps prioritise the next validation slice, such as a channel-assortment mismatch or category-specific product-page issue. |
| **Order lifecycle analysis** | Separate first-purchase conversion from repeat purchase behaviour. | `vw_fact_sales_enriched.sql` labels immediate first purchase, delayed first purchase, and repeat purchase. | The model distinguishes when completed orders occur in the customer lifecycle. | Makes it possible to diagnose first-order friction separately from retention and repeat-order performance. |

### Implemented versus planned analysis

**Implemented:** descriptive KPI/trend analysis; distinct-session funnel measurement; event-sequence and cart-to-checkout behavioural measures; purchase and activity churn segmentation; customer spending and product price-tier segmentation; order-lifecycle tagging; and diagnostic comparison fields in the Power BI model.

**Planned / not yet presented as completed:** finished funnel, customer-health, and channel-to-assortment dashboard pages; independent validation of all legacy blueprint results against the Cartiva warehouse; controlled experiments to test suspected causes; and ongoing analysis as new findings emerge. The available source supports patterns and candidate questions, not proof of causality.

## SQL development

The three view definitions in [`SQL/`](SQL) preserve the original project logic:

- `vw_dim_users_enriched.sql` calculates completed-order history, lifetime value, recency, a global median inter-purchase benchmark, and `Active` / `At-Risk` / `Churned` / `Never Bought` purchase statuses.
- `vw_fact_events_enriched.sql` maps event names to funnel order and assigns an event sequence within each session.
- `vw_fact_sales_enriched.sql` assigns `Immediate First Purchase`, `Delayed First Purchase`, and `Repeat Purchase` tags to completed orders.

## Python ETL pipeline

The runnable entry point is [`Python/main.py`](Python/main.py). It imports the extract, transform, and load modules in sequence. The database helper prompts locally for a MySQL password; no password is stored in this repository.

```bash
pip install -r Python/requirements.txt
python Python/main.py
```

The separate [`Python/import_mysql.py`](Python/import_mysql.py) is a data-preparation utility that generates linked orders, order items, and purchase events for sampled checkout sessions. It is not invoked by `main.py`.

## Power BI dashboard

This repository contains a Power BI Project rather than a single `.pbix` file. Its editable report and semantic-model metadata are retained in `Cartiva.Report/`, `Cartiva.SemanticModel/`, and `Cartiva.pbip`.

### Completed: Overview

The Overview page uses a custom Cartiva layout and contains KPI cards for Total Revenue, Completed Orders, Average Order Value, and Buyer Conversion %. It also includes a monthly revenue/orders trend selector, traffic-source session distribution, a customer-health selector, churn-status session distribution, and a bar chart that highlights View Item -> Add to Cart and Add to Cart -> Begin Checkout leakage.

### In development

The project metadata includes exploratory supporting pages for funnel segmentation, View-to-Cart cuts by device/channel/product/category, and customer health. These pages are not presented as finished dashboard pages. An empty fifth page also remains in the PBIP project and is intentionally left as work in progress.

## Key analytical findings

The measurements below are drawn from the supplied [legacy strategy blueprint](Documentation/Nile_Express_Strategic_Funnel_and_Retention_Blueprint.pdf). The source document is branded **Nile Express**, not Cartiva, and no raw dataset is included in this repository to independently recompute its values. They are therefore documented as **reported findings awaiting Cartiva validation**, not newly calculated Cartiva results.

| Business question | Reported finding | Interpretation / next action |
| --- | --- | --- |
| Where is the main top-funnel loss? | View Item -> Add to Cart leakage was reported at **37.46%**. Furniture (**48.73%**) and Beauty (**47.73%**) were called out as higher-leakage categories. | Prioritise product-page evidence and UX testing; category-specific causes are hypotheses until event and UX research validate them. |
| Where is high-intent demand lost? | Add to Cart -> Begin Checkout leakage was reported at **50.96%**; the blueprint reported **78.89%** for a first-time/non-buyer segment. | Test guest checkout, transparent shipping, and targeted first-order incentives. The proposed causes need checkout and experiment evidence. |
| Does acquisition fit assortment? | Paid Search on Premium was reported at **37.81%** View-to-Cart leakage, while Referral was described as the lowest-leakage channel for Entry-Level/Core tiers. | Validate with channel x price-tier cuts before reallocating acquisition spend. |
| What is the longer-term retention risk? | The blueprint reported 1,990 Never Bought x Activity Churned prospects and 1,641 permanently lost buyers. | Use the model's dual purchase/activity churn views to prioritise reactivation and diagnose first-order failure. |

The exact DAX model supports these analyses with session-distinct funnel measures, stage and cumulative leakage, product-tier leakage, cart-to-checkout elapsed time, customer purchase rate, revenue, orders, AOV, median-based purchase churn, and activity churn.

## Repository structure

```text
.
├── Cartiva.pbip
├── Cartiva.Report/                 # Power BI report definition and resources
├── Cartiva.SemanticModel/          # Power BI TMDL semantic model
├── Dashboard Designs/
│   └── Cartiva_Overview_Wireframe.png
├── Documentation/
│   ├── Cartiva_Project_Summary_and_Key_Insights.pdf
│   └── Nile_Express_Strategic_Funnel_and_Retention_Blueprint.pdf
├── Python/
│   ├── main.py
│   ├── data_extraction.py
│   ├── Data_cleaning.py
│   ├── data_loading.py
│   ├── database.py
│   ├── import_mysql.py
│   └── requirements.txt
└── SQL/
    ├── vw_dim_users_enriched.sql
    ├── vw_fact_events_enriched.sql
    └── vw_fact_sales_enriched.sql
```

## Current status

**Status: In Progress.** The Overview page is complete. The analytical and dashboard development process is ongoing: existing supporting pages are exploratory, further questions and report pages are planned, and the project will continue to evolve as the underlying findings are validated and extended.

## Future development plans

- Validate legacy blueprint metrics against the Cartiva warehouse and reconcile the project naming.
- Complete the funnel, customer lifecycle, and channel/assortment report pages.
- Add data-quality checks and safer configuration for warehouse connection settings.
- Add documented refresh instructions and, where appropriate, non-sensitive sample data or reproducible data-generation steps.
