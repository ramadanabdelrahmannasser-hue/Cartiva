CREATE OR REPLACE VIEW vw_fact_sales_enriched AS

WITH

-- 1. Get distinct completed orders at order level
Distinct_Completed_Orders AS (
    SELECT DISTINCT
        order_id,
        user_id,
        order_date
    FROM fact_sales
    WHERE order_status = 'Completed'
),

-- 2. Sequence completed orders for each customer
Completed_Order_Metrics AS (
    SELECT
        order_id,
        user_id,

        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY order_date, order_id
        ) AS completed_order_seq

    FROM Distinct_Completed_Orders
)

-- 3. Add only the lifecycle classification to the original fact table
SELECT
    fs.*,

    CASE
        WHEN fs.order_status <> 'Completed'
            THEN NULL

        WHEN com.completed_order_seq = 1
         AND DATE_FORMAT(fs.order_date, '%Y-%m')
             = DATE_FORMAT(u.signup_date, '%Y-%m')
            THEN 'Immediate First Purchase'

        WHEN com.completed_order_seq = 1
         AND DATE_FORMAT(fs.order_date, '%Y-%m')
             > DATE_FORMAT(u.signup_date, '%Y-%m')
            THEN 'Delayed First Purchase'

        WHEN com.completed_order_seq > 1
            THEN 'Repeat Purchase'

    END AS order_lifecycle_tag

FROM fact_sales fs

LEFT JOIN dim_users u
    ON fs.user_id = u.user_id

LEFT JOIN Completed_Order_Metrics com
    ON fs.order_id = com.order_id;