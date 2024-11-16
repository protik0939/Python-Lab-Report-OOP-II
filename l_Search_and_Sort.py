# Scenario: You have a dataset representing student scores in various exams stored in an array.
# You need to locate specific scores and arrange the data in ascending or descending order.
#---------------------------
# Question:
# Given a 1D NumPy array of scores, write code to:
# ● Search for specific scores (e.g., 75 and 90) and return their indices.
# ● Sort the array in ascending and descending order.
# Demonstrate both operations and provide examples.
#---------------------------
# Answer:
#---------------------------


import numpy as np

# Sample student scores array
scores = np.array([85, 92, 75, 90, 60, 78, 88, 95, 80, 70])

# Search for specific scores (e.g., 75 and 90) and return their indices
indices_75 = np.where(scores == 75)[0]  # Index of score 75
indices_90 = np.where(scores == 90)[0]  # Index of score 90

# Sort the array in ascending and descending order
sorted_ascending = np.sort(scores)
sorted_descending = np.sort(scores)[::-1]

# Display results
print("Original Scores:", scores)
print("Indices of score 75:", indices_75)
print("Indices of score 90:", indices_90)
print("Sorted Scores (Ascending):", sorted_ascending)
print("Sorted Scores (Descending):", sorted_descending)
