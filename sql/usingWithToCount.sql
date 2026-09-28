WITH totals AS (  
    SELECT app_id,
    sum(
        CASE
            WHEN event_type='click' THEN 1
        ELSE 0
        END
    ) AS total_clicks,
    sum(
        CASE
            WHEN event_type='impression' THEN 1
        ELSE 0
        END
    ) AS total_impressions
    FROM events
    WHERE EXTRACT(YEAR FROM timestamp) = 2022
    GROUP BY app_id
)

SELECT app_id, round(100.0*total_clicks/total_impressions, 2) AS ctr 
FROM totals;
