-- total number of events
SELECT COUNT(*) FROM events;

-- unique users
SELECT COUNT(DISTINCT user_id)
FROM events;

-- unique sessions
SELECT COUNT(DISTINCT user_session)
FROM events;

-- unique products
SELECT COUNT(DISTINCT product_id)
FROM events;

-- time range
SELECT
MIN(event_time),
MAX(event_time)
FROM events;