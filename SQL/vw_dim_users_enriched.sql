CREATE OR REPLACE VIEW vw_dim_users_enriched AS

WITH 

-- 1. Deduplicate from item-grain to order-grain for accurate gap calculation
Successful_Orders AS (
    SELECT DISTINCT
        order_id,
        user_id,
        order_date
    FROM fact_sales
    WHERE order_status = 'Completed'
),

-- 2. Calculate Inter-Purchase Dormancy at the order level
User_Order_Dormancy AS (
    SELECT
        user_id,
        DATEDIFF(
            order_date,
            LAG(order_date) OVER (
                PARTITION BY user_id
                ORDER BY order_date, order_id
            )
        ) AS dormancy_days
    FROM Successful_Orders
),

-- 3. Remove NULL values (first orders have no previous order)
Valid_Dormancy_Gaps AS (
    SELECT dormancy_days
    FROM User_Order_Dormancy
    WHERE dormancy_days IS NOT NULL
),

-- 4. Rank Dormancy Values to find the middle point
Ranked_Dormancy AS (
    SELECT
        dormancy_days,
        ROW_NUMBER() OVER (ORDER BY dormancy_days) AS row_num,
        COUNT(*) OVER () AS total_rows
    FROM Valid_Dormancy_Gaps
),

-- 5. Calculate Global Median across all valid order gaps
Global_Median AS (
    SELECT
        AVG(dormancy_days) AS median_dormancy_days
    FROM Ranked_Dormancy
    WHERE row_num IN (
        FLOOR((total_rows + 1) / 2),
        CEIL((total_rows + 1) / 2)
    )
),

-- 6. Aggregate Customer Sales Metrics (Using DISTINCT order_id to avoid counting items)
User_Sales_Summary AS (
    SELECT
        user_id,
        MIN(order_date) AS first_completed_date,
        MAX(order_date) AS last_completed_date,
        COUNT(DISTINCT order_id) AS total_completed_orders,
        SUM(line_amount) AS total_lifetime_value
    FROM fact_sales
    WHERE order_status = 'Completed'
    GROUP BY user_id
),

-- 7. Define Analysis Snapshot Date
Dataset_Max_Date AS (
    SELECT DATE('2026-06-30') AS current_db_date
)

-- 8. Final Customer Enrichment and Dynamic Churn Segmentation
SELECT
    u.*,

    COALESCE(uss.total_completed_orders, 0) AS total_completed_orders,
    COALESCE(uss.total_lifetime_value, 0) AS total_lifetime_value,

    uss.first_completed_date,
    uss.last_completed_date,

    DATEDIFF(
        dmd.current_db_date,
        uss.last_completed_date
    ) AS recency_days,

    ROUND(gm.median_dormancy_days, 0) AS benchmark_median,

    -- Apply strict segmentation rules: Active (< Median), At-Risk (Median to 2x Median), Churned (> 2x Median)
    CASE
        WHEN uss.user_id IS NULL
            THEN 'Never Bought'

        WHEN DATEDIFF(
            dmd.current_db_date,
            uss.last_completed_date
        ) < gm.median_dormancy_days
            THEN 'Active'

        WHEN DATEDIFF(
            dmd.current_db_date,
            uss.last_completed_date
        ) <= gm.median_dormancy_days * 2
            THEN 'At-Risk'

        ELSE 'Churned'
    END AS dynamic_churn_status

FROM dim_users u

LEFT JOIN User_Sales_Summary uss
    ON u.user_id = uss.user_id

CROSS JOIN Dataset_Max_Date dmd

CROSS JOIN Global_Median gm;