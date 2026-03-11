WITH user_funnel AS (

SELECT
user_id,

MAX(CASE WHEN event_type='view' THEN 1 ELSE 0 END) AS viewed,
MAX(CASE WHEN event_type='cart' THEN 1 ELSE 0 END) AS cart,
MAX(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) AS purchase

FROM events
GROUP BY user_id

)

SELECT
SUM(viewed) AS view_users,
SUM(cart) AS cart_users,
SUM(purchase) AS purchase_users
FROM user_funnel;

-- Conversion
WITH user_funnel AS (

SELECT
user_id,

MAX(CASE WHEN event_type='view' THEN 1 ELSE 0 END) AS viewed,
MAX(CASE WHEN event_type='cart' THEN 1 ELSE 0 END) AS cart,
MAX(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) AS purchase

FROM events
GROUP BY user_id

)

SELECT
SUM(cart)*1.0/SUM(viewed) AS view_to_cart_conversion,
SUM(purchase)*1.0/SUM(cart) AS cart_to_purchase_conversion,
SUM(purchase)*1.0/SUM(viewed) AS overall_conversion
FROM user_funnel;