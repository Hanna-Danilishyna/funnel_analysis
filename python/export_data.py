import pandas as pd
import psycopg2
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data/processed"

OUTPUT_DIR.mkdir(exist_ok=True)


conn = psycopg2.connect(
    dbname="funnel_analysis",
    user="ankapdf",
    host="localhost",
    port="5432"
)


# 1. USER FUNNEL


funnel_query = """

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
SUM(purchase) AS purchase_users,

SUM(cart)*1.0 / SUM(viewed) AS view_to_cart,
SUM(purchase)*1.0 / SUM(cart) AS cart_to_purchase,
SUM(purchase)*1.0 / SUM(viewed) AS overall_conversion

FROM user_funnel

"""

funnel_df = pd.read_sql(funnel_query, conn)

funnel_df.to_csv(
    OUTPUT_DIR / "funnel_metrics.csv",
    index=False
)

print("Exported: funnel_metrics.csv")



# 2. TOP PRODUCTS


top_products_query = """

SELECT

brand,

SUM(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) AS purchase_count,
AVG(price) AS avg_price

FROM events

GROUP BY brand

ORDER BY purchase_count DESC

LIMIT 50

"""

top_products_df = pd.read_sql(top_products_query, conn)

top_products_df = top_products_df[top_products_df["brand"] != "unknown"]

top_products_df.to_csv(
    OUTPUT_DIR / "top_products.csv",
    index=False
)

print("Exported: top_products.csv")



# 3. CATEGORY PERFORMANCE


category_query = """

SELECT

category_code,

SUM(CASE WHEN event_type='view' THEN 1 ELSE 0 END) AS views,
SUM(CASE WHEN event_type='cart' THEN 1 ELSE 0 END) AS carts,
SUM(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) AS purchases,
AVG(price) AS avg_price

FROM events

GROUP BY category_code

ORDER BY purchases DESC

"""

category_df = pd.read_sql(category_query, conn)

category_df.to_csv(
    OUTPUT_DIR / "category_performance.csv",
    index=False
)

print("Exported: category_performance.csv")



# 4. HOURLY USER BEHAVIOR


hour_query = """

SELECT

hour,

COUNT(*) AS events,
SUM(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) AS purchases

FROM events

GROUP BY hour

ORDER BY hour

"""

hour_df = pd.read_sql(hour_query, conn)

hour_df.to_csv(
    OUTPUT_DIR / "hourly_behavior.csv",
    index=False
)

print("Exported: hourly_behavior.csv")



# 5. WEEKDAY BEHAVIOR


weekday_query = """

SELECT

weekday,

COUNT(*) AS events,
SUM(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) AS purchases

FROM events

GROUP BY weekday

"""

weekday_df = pd.read_sql(weekday_query, conn)

weekday_df.to_csv(
    OUTPUT_DIR / "weekday_behavior.csv",
    index=False
)

print("Exported: weekday_behavior.csv")


print("\nAll tables exported successfully.")
