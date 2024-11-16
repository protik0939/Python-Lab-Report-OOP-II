# Scenario: You’re working with data that was initially stored as strings in a CSV file and
# imported into a NumPy array. Now, you need to convert specific columns to integers or floats to
# perform calculations.
#---------------------------
# Question:
# Given a 2D NumPy array with string values, write code to:
# ● Convert an entire column to integer type if it represents whole numbers (e.g., age data).
# ● Convert a column to float type if it represents decimal values (e.g., salary or price).
# Demonstrate the type casting on a sample NumPy array.
#---------------------------
# Answer:
#---------------------------


import numpy as np

# Sample 2D array with string values (e.g., names, age, salary)
data = np.array([
    ["Alice", "25", "50000.50"],  # Name, Age (String), Salary (String)
    ["Bob", "30", "60000.75"],
    ["Charlie", "35", "70000.25"]
], dtype='str')  # dtype is 'str' because data is initially imported as strings

# 1. Convert the 'Age' column (index 1) to integers
ages = data[:, 1].astype(int)  # Convert the second column to integers
print("Converted Age column to integers:")
print(ages)

# 2. Convert the 'Salary' column (index 2) to floats
salaries = data[:, 2].astype(float)  # Convert the third column to floats
print("\nConverted Salary column to floats:")
print(salaries)
