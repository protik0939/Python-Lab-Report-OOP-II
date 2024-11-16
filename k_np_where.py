# Scenario: You’re analyzing temperatures recorded over several days. You want to identify days
# when the temperature exceeded a certain threshold and replace any low temperatures with a
# specified minimum value.
#---------------------------
# Question:
# Given a NumPy array of temperatures, write code to:
# ● Use np.where to find indices where the temperature exceeds a certain threshold.
# ● Use np.where to replace temperatures below a certain threshold with a minimum
# value.
# Demonstrate this operation with a sample temperature array.
#---------------------------
# Answer:
#---------------------------


import numpy as np

# Sample temperature data (in degrees Celsius) for several days
temperatures = np.array([15, 22, 30, 18, 25, 10, 5, 28, 32, 14])

# Define threshold and minimum value
threshold = 20
min_value = 10

# Find indices where temperature exceeds the threshold
indices_above_threshold = np.where(temperatures > threshold)

# Replace temperatures below the threshold with the minimum value
temperatures_corrected = np.where(temperatures < threshold, min_value, temperatures)

# Display results
print("Original Temperatures:", temperatures)
print("Indices where temperature exceeds the threshold:", indices_above_threshold)
print("Temperatures after replacing those below threshold with minimum value:", temperatures_corrected)
