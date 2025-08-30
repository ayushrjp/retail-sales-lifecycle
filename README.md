Retail Sales Data Lifecycle Project
Overview

This mini-project demonstrates a complete data lifecycle in the retail domain:

Capture → Raw sales data (data/raw/sales.csv).

Store → Organize data in data/raw/ and save processed results in data/processed/.

Process → Clean data, calculate revenue, detect low-stock products.

Visualize → Generate charts for daily sales trends and top-selling products.

Project Structure
retail-sales-lifecycle/
├── data/
│   ├── raw/                 # Raw sales CSV
│   └── processed/           # Processed CSV and charts
├── src/                     # Python scripts
│   └── process_sales.py     # Main processing script
├── notebooks/               # Optional Jupyter notebooks
├── README.md                # Project overview
├── requirements.txt         # Python dependencies

Setup & Run

Clone the repository:

git clone https://github.com/YOUR_USERNAME/retail-sales-lifecycle.git
cd retail-sales-lifecycle


Install dependencies:

pip install -r requirements.txt


Run the processing script:

python src/process_sales.py


Check results in data/processed/:

sales_processed.csv → cleaned dataset with revenue

daily_sales.png → daily sales trend chart

top_products.png → top selling products chart

Sample Output
Daily Sales Trend

Top Selling Products

Low Stock Alerts

Products with stock < 10 will be printed in the console.

Dependencies

Python 3.x

pandas

matplotlib

Install via:

pip install -r requirements.txt
