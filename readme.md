# E-commerce User Behavior & Conversion Funnel Analysis

## Project Overview

This project analyzes **user interaction data from an e-commerce platform** to understand how customers move through the purchasing process and what factors influence conversions.

The analysis focuses on:

- user behavior across the **purchase funnel**
- **top selling brands and products**
- **category-level performance**
- **temporal patterns** in user activity

The goal is to identify **conversion bottlenecks**, uncover **high-performing product segments**, and derive **data-driven business insights**.

---

# Dataset

This project uses the **E-commerce Behavior Data from Multi-Category Store** dataset.

The dataset contains **millions of user interaction events** collected from an online store, including:

- product views
- add-to-cart actions
- purchases

Each event contains:

- event type
- product category
- brand
- product price
- timestamp
- user session data

Dataset source:

https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store

Due to GitHub file size limitations, the full dataset is **not included in this repository**.

---

# Tech Stack

Python

Libraries used:

- pandas
- numpy
- matplotlib
- seaborn

---

# Project Structure
```
funnel_analysis
  data
    raw
    processed

  plots
    user_funnel.png
    top_products.png
    avg_price_by_brand.png

  python
    cleaned_events_sample.py
    data_cleaning.py
    export_data.py
    funnel_analysis.py
    product_analysis.py
    visualization.png


  sql
    01_data_exploration.sql
    02_event_distribution.sql
    03_funnel_analysis.sql
    04_product_analysis.sql
    05_revenue_metrics.sql

README.md
```


---

# Analysis

The analysis consists of several key components.

---

# Conversion Funnel Analysis

<p align="center">
  <img src="plots/user_funnel.png" width="700">
</p>

User progression through the purchase funnel:

| Stage | Users |
|-----|------|
Product Views | 406,863 |
Add to Cart | 36,952 |
Purchases | 21,304 |

Conversion rates:

- **View → Cart:** 9.08%
- **Cart → Purchase:** 57.65%
- **Overall Conversion:** 5.24%

### Key Insight

The largest drop-off occurs between **product view and add-to-cart**.

This suggests potential improvements in:

- product page UX
- product descriptions and images
- pricing perception
- recommendation systems

Interestingly, the **cart → purchase conversion rate is very high**, indicating that once users commit to a product, they are highly likely to complete the purchase.

---

#  Top Brands by Purchases

<p align="center">
  <img src="plots/top_products.png" width="700">
</p>

The chart highlights brands with the highest number of purchases.

Top performers include:

- MSI
- Gigabyte
- Asus
- Palit

These brands primarily belong to the **computer hardware segment**, particularly **graphics cards**, indicating strong demand for high-performance computing components.

---

#  Average Price by Brand

<p align="center">
  <img src="plots/avg_price_by_brand.png" width="700">
</p>

This visualization compares the **average price of products across brands**.

Key observations:

- **Palit** has the highest average product price (~$467)
- **MSI** and **Gigabyte** combine high price points with high sales volume
- Some lower-priced brands generate high purchase counts due to accessibility

This demonstrates the coexistence of **premium and budget segments** in the market.

---

#  Category Performance

Category-level analysis reveals which product segments drive the most engagement and purchases.

Top performing categories include:

| Category | Purchases |
|--------|---------|
Computers → Components → Video Cards | 6888 |
Electronics → Telephones | 4119 |
Stationery → Cartridges | 2739 |
Computers → Printers | 2557 |

### Key Insights

**Graphics cards dominate the platform in both demand and price**, making them a major revenue driver.

Printer cartridges show **high purchase conversion**, likely because customers often search for a specific compatible product.

---

#  Temporal Behavior Analysis

User activity varies significantly by time of day.

Peak purchase hours:

**09:00 – 12:00**

User activity gradually decreases in the evening.

### Weekly Behavior

Purchases remain relatively consistent across weekdays, with slightly higher activity early in the week:

- Monday
- Tuesday
- Wednesday

This suggests that many users browse and purchase products during **working hours or daytime browsing sessions**.

---

#  Business Insights

Based on the analysis, several key insights emerge.

### 1️. Conversion Bottleneck

The largest user drop-off occurs before items are added to the cart.

Potential improvements:

- improve product page design
- enhance product recommendations
- provide better product information

---

### 2️. High-Value Product Segments

The most valuable product segments include:

- graphics cards
- computer components
- electronics

Marketing and inventory strategies should prioritize these categories.

---

### 3️. Timing for Marketing Campaigns

Promotional campaigns and advertising could be optimized for peak activity hours:

**09:00 – 12:00**

---

# Future Improvements

Potential extensions of this analysis include:

- cohort analysis
- customer segmentation
- revenue forecasting
- recommendation system prototype
- A/B testing simulations

---

# Author

Data analysis project created as part of a **Data Analytics portfolio**.
