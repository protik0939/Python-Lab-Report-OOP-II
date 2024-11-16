# Scenario: You have a 2D NumPy array representing sales data, where each row is a product, and
# columns represent sales over several months. You need to analyze sales for specific months and
# products.
#---------------------------
# Question:
# Given a 2D array of sales data, write code to extract:
# ● Sales data for the first three products.
# ● Sales data for all products in the last two months.
# ● Sales data for a specific product and month (e.g., 2nd product in the 4th month).
# Demonstrate these operations on a sample 2D array.
#---------------------------
# Answer:
#---------------------------


import numpy as np

# Sample sales data (rows: products, columns: months)
sales_data = np.array([
    [500, 600, 700, 800],  # Product 1 sales for months 1 to 4
    [300, 400, 500, 600],  # Product 2 sales for months 1 to 4
    [700, 800, 900, 1000], # Product 3 sales for months 1 to 4
    [100, 150, 200, 250],  # Product 4 sales for months 1 to 4
    [1200, 1300, 1400, 1500] # Product 5 sales for months 1 to 4
])

# 1. Sales data for the first three products
first_three_products = sales_data[:3, :]
print("Sales data for the first three products:")
print(first_three_products)

# 2. Sales data for all products in the last two months (months 3 and 4)
last_two_months_sales = sales_data[:, -2:]
print("\nSales data for all products in the last two months:")
print(last_two_months_sales)

# 3. Sales data for the 2nd product in the 4th month
specific_product_month_sales = sales_data[1, 3]
print("\nSales data for the 2nd product in the 4th month:")
print(specific_product_month_sales)
