-- Q: users that posted more than 2 times in 2021, give us the days between first and their last post?
SELECT 
user_id,
EXTRACT(DAY FROM max(post_date) - min(post_date)) AS difference  -- time difference in days
FROM posts
WHERE EXTRACT(YEAR FROM post_date) = 2021  -- year 2021
GROUP BY user_id
HAVING count(*) >= 2;  -- more than 2 posts
