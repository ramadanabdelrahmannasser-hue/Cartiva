
CREATE OR REPLACE VIEW vw_fact_events_enriched AS

WITH

-- 1. Map events to their respective funnel stages
Event_Funnel_Mapping AS (
    SELECT
        *,
        CASE event_name
            WHEN 'session_start'  THEN 1
            WHEN 'page_view'      THEN 2
            WHEN 'view_item'      THEN 3
            WHEN 'add_to_cart'    THEN 4
            WHEN 'begin_checkout' THEN 5
            WHEN 'purchase'       THEN 6
            ELSE 99
        END AS funnel_step_order

    FROM fact_events
),

-- 2. Sequence events chronologically within each session
Session_Funnel_Sequence AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY session_id
            ORDER BY event_date, event_time, event_id
        ) AS event_seq_in_session

    FROM Event_Funnel_Mapping
)

-- 3. Final enriched event table
SELECT *
FROM Session_Funnel_Sequence;
