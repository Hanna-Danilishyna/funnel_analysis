import pandas as pd
from pathlib import Path
import psycopg2

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "data/processed/funnel_metrics.csv"

conn = psycopg2.connect(
    dbname="funnel_analysis",
    user="ankapdf",
    host="localhost",
    port="5432"
)

query = """

WITH user_funnel AS (

SELECT
user_id,

MAX(CASE WHEN event_type='view' THEN 1 ELSE 0 END) as viewed,
MAX(CASE WHEN event_type='cart' THEN 1 ELSE 0 END) as cart,
MAX(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) as purchase

FROM events
GROUP BY user_id

)

SELECT

SUM(viewed) as view_users,
SUM(cart) as cart_users,
SUM(purchase) as purchase_users,

SUM(cart)*1.0 / SUM(viewed) as view_to_cart,
SUM(purchase)*1.0 / SUM(cart) as cart_to_purchase,
SUM(purchase)*1.0 / SUM(viewed) as overall_conversion

FROM user_funnel;

"""

df = pd.read_sql(query, conn)

print(df)

df.to_csv(OUTPUT_PATH, index=False)

print("Funnel metrics exported:", OUTPUT_PATH)