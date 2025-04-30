import sqlite3
import pandas as pd

conn = sqlite3.connect("../db/lesson.db")
# for terminal
# SELECT c.customer_name, o.order_id FROM customers c LEFT JOIN orders o on c.customer_id = o.customer_id;
# UPDATE products SET price=price * 1.1;
# DELETE FROM products WHERE price<1.0;

query = """
SELECT
    line_item_id,
    quantity,
    p.product_id,
    product_name,
    price
FROM line_items li
JOIN products p ON li.product_id = p.product_id
"""

df = pd.read_sql_query(query, conn)
print("Initial DataFrame:\n", df.head())

df['total'] = df['quantity'] * df['price']
print("\nWith Total Column:\n", df.head())

summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).reset_index()

summary = summary.sort_values(by='product_name')
print("\nGrouped Summary:\n", summary.head())

summary.to_csv("order_summary.csv", index=False)
print("\nSummary saved to order_summary.csv")
