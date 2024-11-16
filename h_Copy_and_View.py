# Scenario: You have a large dataset in a NumPy array and want to perform operations on a subset
# without modifying the original data. You’re unsure whether to use a copy or view.
#---------------------------
# Question:
# Given a 2D array of data, write code to:
# ● Create a view of a specific row.
# ● Create a deep copy of a specific column.
# ● Modify both the view and the copy, and observe which one affects the original array.
# Explain the difference in behavior between the copy and view based on your code.
#---------------------------
# Answer:
#---------------------------


import numpy as np

# Sample 2D array with data (e.g., student ID, scores, age)
data = np.array([
    [1, 90, 21],   # Student 1 (ID, Score, Age)
    [2, 85, 22],   # Student 2
    [3, 88, 23],   # Student 3
    [4, 92, 24]    # Student 4
])

# 1. Create a view of the second row (index 1)
view_of_row = data[1, :]
print("Original data (before modification):")
print(data)

# 2. Create a deep copy of the first column (index 0)
copy_of_column = data[:, 0].copy()

# Modify the view (change the second row's scores)
view_of_row[1] = 100  # Modify the score of the second student
print("\nData after modifying the view:")
print(data)

# Modify the copy (change the first column values)
copy_of_column[0] = 999  # Modify the first student's ID
print("\nData after modifying the copy:")
print(data)

# Print the view and copy for clarity
print("\nView of second row after modification:")
print(view_of_row)

print("\nCopy of the first column after modification:")
print(copy_of_column)
