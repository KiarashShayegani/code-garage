--------------- Some little EDA -----------------------------
-- SELECT count(DISTINCT user_id) as distinct_users
-- FROM viewership;
-- SELECT count(DISTINCT device_type) as devices
-- FROM viewership;
-- SELECT count(DISTINCT view_time) as distinct_viewtime
-- FROM viewership;
-------------------------------------------------------------
SELECT
count(
CASE
  WHEN device_type = 'laptop' THEN 1
  ELSE NULL
END
) AS laptop_views,
count(
CASE
  WHEN device_type IN('phone','tablet') THEN 1
  ELSE NULL
END
) AS mobile_views
FROM viewership;
