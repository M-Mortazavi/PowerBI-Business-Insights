"""
Power BI Business Insights - Data Cleaning Script
--------------------------------------------------
This script cleans and processes multiple datasets for use in Power BI.
It ensures data consistency, corrects data types, handles missing values, 
and exports cleaned data for further analysis.

Author: [Morteza Mortazavi]
GitHub: [https://github.com/M-Mortazavi]
"""

# Import required libraries
import pandas as pd
import os

# Set display options for Pandas
pd.set_option('display.max_rows', None)

# Define file paths (Update these paths as needed)
DATA_DIR = r"C:\D drive\Dars\France master\OneDrive\Caen Master\credentials and documents\Resume\CV\Data Projects\Online shop\Data sets\\"
OUTPUT_DIR = DATA_DIR + "cleaned data sets\\"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load datasets
print("Loading datasets...")
customers = pd.read_csv(DATA_DIR + "customers.csv")
order_items = pd.read_csv(DATA_DIR + "order_items.csv")
orders = pd.read_csv(DATA_DIR + "orders.csv")
payment = pd.read_csv(DATA_DIR + "payment.csv")
products = pd.read_csv(DATA_DIR + "products.csv")
reviews = pd.read_csv(DATA_DIR + "reviews.csv")
shipments = pd.read_csv(DATA_DIR + "shipments.csv")
suppliers = pd.read_csv(DATA_DIR + "suppliers.csv")

print("Datasets loaded successfully!")

# ------------------------------
# 🛠️ Data Cleaning & Transformation
# ------------------------------

# 🔹 Step 1: Handle Duplicate Phone Numbers in Customers
print("Checking for duplicate phone numbers...")
duplicate_phone_numbers = customers[customers.duplicated(subset=['phone_number'], keep=False)]
if not duplicate_phone_numbers.empty:
    print("Duplicate phone numbers found. Resolving...")
    customers.loc[customers.duplicated(subset=['phone_number'], keep=False), 'phone_number'] = \
        "RP-" + customers.loc[customers.duplicated(subset=['phone_number'], keep=False), 'phone_number']
    print("Duplicate phone numbers resolved.")

# 🔹 Step 2: Convert Numerical Columns to Integer (Filling Missing Values with 0)
print("Converting numerical columns to integer...")
order_items['price_at_purchase'] = order_items['price_at_purchase'].fillna(0).astype(int)
orders['total_price'] = orders['total_price'].fillna(0).astype(int)
payment['amount'] = payment['amount'].fillna(0).astype(int)
products['price'] = products['price'].fillna(0).astype(int)
print("Numerical conversion completed.")

# 🔹 Step 3: Convert Date Columns to Datetime Format
print("Converting date columns...")
orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
shipments['delivery_date'] = pd.to_datetime(shipments['delivery_date'], errors='coerce')
shipments['shipment_date'] = pd.to_datetime(shipments['shipment_date'], errors='coerce')
print("Date conversion completed.")

# ------------------------------
# 🔍 Validate Data Types
# ------------------------------
print("\n🔍 Validating Data Types After Cleaning...\n")
datasets = {
    "Customers": customers,
    "Order Items": order_items,
    "Orders": orders,
    "Payment": payment,
    "Products": products,
    "Reviews": reviews,
    "Shipments": shipments,
    "Suppliers": suppliers
}

for name, df in datasets.items():
    print(f"\n{name} Dataset:")
    print(df.info())

# ------------------------------
# 📤 Export Cleaned Datasets
# ------------------------------
print("\n📤 Exporting Cleaned Data...")
customers.to_csv(OUTPUT_DIR + 'customers.csv', index=False)
order_items.to_csv(OUTPUT_DIR + 'order_items.csv', index=False)
orders.to_csv(OUTPUT_DIR + 'orders.csv', index=False)
payment.to_csv(OUTPUT_DIR + 'payment.csv', index=False)
products.to_csv(OUTPUT_DIR + 'products.csv', index=False)
reviews.to_csv(OUTPUT_DIR + 'reviews.csv', index=False)
shipments.to_csv(OUTPUT_DIR + 'shipments.csv', index=False)
suppliers.to_csv(OUTPUT_DIR + 'suppliers.csv', index=False)

print("\n✅ Data Cleaning & Export Completed Successfully!")
