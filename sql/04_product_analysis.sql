-- top categories by views

SELECT
category_code,
COUNT(*) AS views
FROM events
WHERE event_type='view'
GROUP BY category_code
ORDER BY views DESC
LIMIT 20;


-- top brands by purchases

SELECT
brand,
COUNT(*) AS purchases
FROM events
WHERE event_type='purchase'
GROUP BY brand
ORDER BY purchases DESC
LIMIT 20;