import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://<YOUR_USERNAME>@localhost:5432/sales_analysis",
    connect_args={"password": "<YOUR_PASSWORD>"}
)

query = """
WITH stats AS (
    SELECT
        AVG(sales) AS avg_sales,
        STDDEV(sales) AS std_sales,
        AVG(discount) AS avg_discount
    FROM sales
)
SELECT
    order_id,
    customer_id,
    sales,
    discount,
    profit,
    CASE
        WHEN sales > (avg_sales + 3 * std_sales)
            THEN 'High Value Order'
        WHEN discount > (avg_discount * 2)
            AND profit < 0
            THEN 'High Discount, Low Profit'
        ELSE 'Normal'
    END AS anomaly_type
FROM sales
CROSS JOIN stats;
"""

df = pd.read_sql(query, engine)

# Plot anomaly distribution
df['anomaly_type'].value_counts().plot(kind='bar')
plt.title("Transaction Anomaly Distribution")
plt.xlabel("Anomaly Type")
plt.ylabel("Number of Transactions")
plt.show()


# Sales Distribution with Threshold

avg_sales = df['sales'].mean()
std_sales = df['sales'].std()
threshold = avg_sales + 3 * std_sales

plt.hist(df['sales'], bins=50)
plt.axvline(threshold, linestyle='--')
plt.title("Sales Distribution with Anomaly Threshold")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.show()


# 3. Discount vs Profit Scatter

scatter_query = """
SELECT
    discount,
    profit
FROM sales
WHERE profit IS NOT NULL
"""

scatter_df = pd.read_sql(scatter_query, engine)

plt.scatter(
    scatter_df['discount'],
    scatter_df['profit'],
    alpha=0.5
)

plt.axhline(0, linestyle='--') 
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()
