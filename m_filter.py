# Scenario: You have an array representing product prices, and you need to filter out products that
# fall within a certain price range for a sale promotion.
#---------------------------
# Question:
# Given a 1D array of product prices, write code to:
# ● Use boolean indexing to filter products within a specified price range (e.g., between $20
# and $50).
# ● Display only the filtered prices.
# Demonstrate the filtering with a sample price array.
#---------------------------
# Answer:
#---------------------------


import numpy as np

# Sample product prices array
prices = np.array([15.99, 25.50, 40.75, 60.00, 45.30, 5.99, 30.20, 55.60, 19.99, 50.00])

# Define price range for the sale promotion (e.g., between $20 and $50)
lower_bound = 20
upper_bound = 50

# Use boolean indexing to filter products within the specified price range
filtered_prices = prices[(prices >= lower_bound) & (prices <= upper_bound)]

# Display the filtered prices
print("Filtered Prices:", filtered_prices)
