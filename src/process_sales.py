import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
RAW_DATA_PATH = "../data/raw/sales.csv"
PROCESSED_DATA_PATH = "../data/processed/sales_processed.csv"
CHART_SALES_PATH = "../data/processed/daily_sales.png"
CHART_PRODUCTS_PATH = "../data/processed/top_products.png"

# Ensure processed folder exists
os.makedirs("../data/processed", exist_ok=True)

# Load raw data
df = pd.read_csv(RAW_DATA_PATH)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop any rows with missing values
df = df.dropna()

# Compute revenue
df['Revenue'] = df['Quantity'] * df['Price_per_unit']

# Save processed data
df.to_csv(PROCESSED_DATA_PATH, index=False)

# ----- ANALYSIS -----

# 1. Daily revenue trend
daily_sales = df.groupby('Date')['Revenue'].sum().reset_index()

# 2. Top selling products
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).reset_index()

# 3. Low stock alerts
low_stock = df[df['Stock_Remaining'] < 10][['Product', 'Stock_Remaining']]

# Print summaries
print("📊 Daily Sales:\n", daily_sales)
print("\n🏆 Top Products:\n", top_products)
print("\n⚠️ Low Stock Alerts:\n", low_stock)

# ----- VISUALIZATION -----

# Daily sales trend
plt.figure(figsize=(8, 5))
plt.plot(daily_sales['Date'], daily_sales['Revenue'], marker='o', color='b')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_SALES_PATH)
plt.close()

# Top products bar chart
plt.figure(figsize=(6, 4))
plt.bar(top_products['Product'], top_products['Revenue'], color='green')
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(CHART_PRODUCTS_PATH)
plt.close()

print("\n✅ Processing complete! Check the 'data/processed/' folder for results.")
