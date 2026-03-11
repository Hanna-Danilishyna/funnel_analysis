-- revenue by category

SELECT
category_code,
SUM(price) AS revenue
FROM events
WHERE event_type='purchase'
GROUP BY category_code
ORDER BY revenue DESC;


-- average order value

SELECT
AVG(price)
FROM events
WHERE event_type='purchase';


-- revenue by brand

SELECT
brand,
SUM(price) AS revenue
FROM events
WHERE event_type='purchase'
GROUP BY brand
ORDER BY revenue DESC
LIMIT 20;