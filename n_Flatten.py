# Scenario: You have a 3D array representing data collected from multiple devices over multiple
# days, with each device’s daily data stored in a 2D matrix format. You need to process this data as
# a single list.
#---------------------------
# Question:
# Given a 3D NumPy array, write code to:
# ● Flatten the array into a 1D array.
# ● Explain why flattening might be necessary and what kind of operations it enables.
# Demonstrate this operation with a sample 3D array.
#---------------------------
# Answer:
#---------------------------


import numpy as np

# Sample 3D array representing data collected from 3 devices over 2 days (e.g., 3 devices, each with 2 days of data)
data = np.array([[[5, 6, 7], [8, 9, 10]],
                 [[1, 2, 3], [4, 5, 6]],
                 [[11, 12, 13], [14, 15, 16]]])

# Flatten the 3D array into a 1D array
flattened_data = data.flatten()

# Display the flattened array
print("Flattened Data:", flattened_data)
