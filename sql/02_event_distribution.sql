SELECT
event_type,
COUNT(*) AS events,
COUNT(DISTINCT user_id) AS users
FROM events
GROUP BY event_type
ORDER BY events DESC;