import pandas as pd
from pathlib import Path
import psycopg2

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "data/processed/top_products.csv"

conn = psycopg2.connect(
    dbname="funnel_analysis",
    user="ankapdf",
    host="localhost",
    port="5432"
)

query = """

SELECT

category_code,
brand,

COUNT(DISTINCT product_id) as product_count,

SUM(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) as purchase_count,

AVG(price) as avg_price

FROM events

GROUP BY category_code, brand

ORDER BY purchase_count DESC

LIMIT 20

"""

df = pd.read_sql(query, conn)

print(df.head())

df.to_csv(OUTPUT_PATH, index=False)

print("Product analytics exported:", OUTPUT_PATH)