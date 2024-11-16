# Scenario: You have two arrays representing data from two different branches of a store. To
# analyze combined sales, you need to merge the data by joining arrays along different axes.
#---------------------------
# Question:
# Given two 1D NumPy arrays representing sales, write code to:
# ● Join the arrays horizontally to represent two branches as columns.
# ● Join the arrays vertically to represent two branches as additional rows.
# Demonstrate both types of joins and explain in which scenario each type would be useful.
#---------------------------
# Answer:
#---------------------------


import numpy as np

# Sample sales data for two branches (1D arrays)
branch1_sales = np.array([1000, 1500, 2000, 2500, 3000])
branch2_sales = np.array([1100, 1400, 2100, 2400, 3100])

# Horizontal join (representing two branches as columns)
horizontal_join = np.column_stack((branch1_sales, branch2_sales))

# Vertical join (representing two branches as rows)
vertical_join = np.vstack((branch1_sales, branch2_sales))

# Display the results
print("Horizontal Join (Columns):")
print(horizontal_join)

print("\nVertical Join (Rows):")
print(vertical_join)
