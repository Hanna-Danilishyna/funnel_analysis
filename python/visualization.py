import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import psycopg2

# style
sns.set_style("whitegrid")


BASE_DIR = Path(__file__).resolve().parent.parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

# connect PostgreSQL
conn = psycopg2.connect(
    dbname="funnel_analysis",
    user="ankapdf",
    host="localhost",
    port="5432"
)


# FUNNEL DATA


funnel_query = """

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
SUM(purchase) as purchase_users

FROM user_funnel

"""

funnel_df = pd.read_sql(funnel_query, conn)


# PRODUCT DATA


product_query = """

SELECT

brand,

SUM(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) as purchase_count,
AVG(price) as avg_price

FROM events

GROUP BY brand

ORDER BY purchase_count DESC

LIMIT 20

"""

product_df = pd.read_sql(product_query, conn)

# delete unknown
product_df = product_df[product_df["brand"] != "unknown"]


# USER FUNNEL PLOT


steps = ["view_users", "cart_users", "purchase_users"]
values = funnel_df.loc[0, steps]

plt.figure(figsize=(8,6))

sns.barplot(
    x=steps,
    y=values,
    palette="viridis",
    ci=None
)

plt.title("User Funnel")
plt.ylabel("Users")
plt.xlabel("Funnel Stage")

plt.tight_layout()

plt.savefig(PLOTS_DIR / "user_funnel.png")

plt.close()


# TOP PRODUCTS BY PURCHASES


product_purchase = product_df.sort_values(
    by="purchase_count",
    ascending=False
)

plt.figure(figsize=(10,6))

sns.barplot(
    data=product_purchase,
    x="purchase_count",
    y="brand",
    palette="viridis",
    ci=None
)

plt.title("Top Products by Purchases")
plt.xlabel("Purchase Count")
plt.ylabel("Brand")

plt.tight_layout()

plt.savefig(PLOTS_DIR / "top_products.png")

plt.close()


# AVERAGE PRICE BY BRAND


product_price = product_df.sort_values(
    by="avg_price",
    ascending=False
)

plt.figure(figsize=(10,6))

sns.barplot(
    data=product_price,
    x="avg_price",
    y="brand",
    palette="magma",
    ci=None
)

plt.title("Average Price by Brand")
plt.xlabel("Average Price")
plt.ylabel("Brand")

plt.tight_layout()

plt.savefig(PLOTS_DIR / "avg_price_by_brand.png")

plt.close()

print("Plots saved to:", PLOTS_DIR)
