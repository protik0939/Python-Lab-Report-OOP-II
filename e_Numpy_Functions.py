# Scenario: You are given a dataset of students' scores in different subjects stored in a 2D NumPy
# array, where each row represents a student and each column represents a subject. You need to
# calculate the average score per student and identify the student with the highest average.
#---------------------------
# Question:
# Write a Python function using NumPy to calculate the average score for each student. Then,
# identify the student with the highest average score and print their score. Use appropriate NumPy
# functions to solve this problem efficiently.
#---------------------------
# Answer:
#---------------------------


import numpy as np

def highest_average_student(scores):
    # Calculate the average score for each student (along axis 1, i.e., row-wise)
    averages = np.mean(scores, axis=1)
    
    # Find the index of the student with the highest average score
    highest_avg_index = np.argmax(averages)
    
    # Get the highest average score
    highest_avg_score = averages[highest_avg_index]
    
    # Print the result
    print(f"Student {highest_avg_index + 1} has the highest average score of {highest_avg_score:.2f}")

# Test dataset of students' scores in different subjects (rows: students, columns: subjects)
scores = np.array([
    [85, 90, 78, 92],  # Student 1
    [88, 85, 91, 87],  # Student 2
    [95, 97, 92, 98],  # Student 3
    [80, 85, 88, 82],  # Student 4
])

# Call the function
highest_average_student(scores)
