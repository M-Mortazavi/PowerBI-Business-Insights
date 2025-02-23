# Power BI Business Insights Dashboard – Data-Driven Decision Making
Power BI dashboard for business insights, analyzing sales, and supplier performance using Python and DAX.

This project demonstrates how data analytics can drive business insights using Power BI, Python (Pandas, NumPy), and DAX calculations. The goal is to analyze sales performance, customer behavior, supplier efficiency, and order fulfillment trends by integrating multiple datasets into an interactive dashboard.

✅ Key Business Questions Answered:

* Who are the best-performing suppliers?
* Which products are the top and worst sellers?
* How does customer churn evolve over time?
* What percentage of sales come from new vs. returning customers?
* How long does it take to fulfill an order?
* How does sales performance compare across categories?
📊 This project transforms raw business data into actionable insights with advanced ETL, data modeling, and visualization techniques.

📊 Steps of the Analysis
1️⃣ Business Questions & Objectives
Before starting, I defined the key business problems that this analysis should solve, including sales trends, customer churn, supplier performance, and order fulfillment efficiency.

2️⃣ Data Extraction & Cleaning with Python 🐍
The dataset included 8 different CSV files (Orders, Products, Customers, Suppliers, Shipments, Payments, Order Items, and Reviews).

✔ Checked for inconsistencies in data types (e.g., dates stored as text).
✔ Standardized column names for easy integration.
✔ Handled missing values (e.g., filled null values in transactions).
✔ Removed duplicate records for accurate calculations.
✔ Fixed inconsistent data patterns (e.g., phone numbers, product codes).

📌 Tools Used: Pandas, NumPy, Jupyter Notebook

3️⃣ Data Modeling in Power BI 🔗
After cleaning, the data was imported into Power BI, where I built a star schema model to optimize performance and relationships.

✔ Linked all 8 tables using primary and foreign keys.
✔ Created relationships to enable cross-table analysis.
✔ Optimized queries for faster performance.

📌 Power BI Data Model Includes:

Fact Tables: Orders, Payments, Shipments, Order Items
Dimension Tables: Customers, Products, Suppliers, Reviews
4️⃣ Advanced DAX Measures for Business Insights
💡 Key Calculations Created Using DAX:
✔ Promotion Expenses → (Price - Price at Purchase) * Quantity
✔ Order Fulfillment Time → (Order Date - Shipment Date)
✔ Delta Sales → Comparison with previous periods.
✔ MTD Sales (Month-to-Date) → Tracks sales progress within the current month.
✔ YTD Sales (Year-to-Date) → Aggregates total sales for the current year.
✔ Last 30 Days Sales → Provides recent sales trends.
✔ AOV (Average Order Value) → Adjusts based on selected time period.
✔ Order Frequency Trend → Measures how frequently customers make purchases.
✔ Sales & Sales Evolution Per Category → Compares product categories dynamically.

📌 Tools Used: DAX (Data Analysis Expressions) in Power BI

5️⃣ Interactive Data Visualization in Power BI 📈
The dashboard provides clear, dynamic insights with interactive filters and KPIs.

✔ Sales & Revenue Trend Over Time → Tracks monthly and yearly sales performance.
✔ Top 5 Best-Selling & Worst-Selling Products → Dynamically updates based on filters.
✔ Customer Churn Rate → Displays retention trends over time.
✔ New vs. Returning Customer Sales → Highlights customer loyalty trends.
✔ Supplier Performance Comparison → Shows which suppliers drive the most sales.
✔ Order Fulfillment Performance → Tracks average shipping time and delays.
✔ Category-Level Sales & Sales Evolution → Compares different product categories.
✔ Dynamic KPI Cards → Shows MTD Sales, YTD Sales, Last 30 Days Sales, and AOV.
✔ Custom Slicers & Filters → Allows users to filter by date, product category, supplier, and customer type.

📌 Tools Used: Power BI, DAX, Interactive Filters

6️⃣ Sharing & Deployment 🌍
📌 Power BI Dashboard Link: 🔗 Click Here to Explore the Dashboard

✅ How You Can Use This Dashboard:
✔ Identify sales trends and growth opportunities.
✔ Analyze customer behavior and optimize churn reduction strategies.
✔ Improve supplier selection by tracking performance.
✔ Optimize order fulfillment efficiency based on shipping trends.

🛠️ **Technologies Used**
📊 Power BI (Data Modeling, DAX, Visualizations)
📈 DAX (Data Analysis Expressions)
🐍 Python (Pandas, NumPy for ETL)
🔄 ETL (Extract, Transform, Load) Process
🗂️ Data Modeling & Star Schema
📦 Business Intelligence (BI)
📉 Data Visualization
💡 KPI Reporting

📂 How to Use This Repository
1️⃣ Clone the repository: 
git clone https://github.com/YOUR_GITHUB_USERNAME/PowerBI-Business-Insights-Dashboard.git
2️⃣ Open PowerBI-Dashboard.pbix in Power BI
3️⃣ Run data_cleaning.ipynb (Jupyter Notebook) to clean new data
4️⃣ Explore the interactive Power BI dashboard

🌍 Live Demo & Contributions
📌 Live Dashboard: 🔗 https://community.fabric.microsoft.com/t5/Themes-Gallery/Ecommerce-Dashboard/m-p/4423001#M4431
📌 Contributions Welcome!
If you have ideas for improvement, feel free to fork, explore, and contribute! 🚀

📧 Contact & Feedback
If you find this project useful or have suggestions, connect with me on:
📩 Email: [MortezaMortazavi000@gmail.com]
🔗 LinkedIn: https://www.linkedin.com/in/seyed-morteza-mortazavi-11b643a5/
