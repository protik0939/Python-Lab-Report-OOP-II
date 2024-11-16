# Scenario: You have a 1D array representing data from multiple sensors over a period. To
# perform matrix operations, you need to restructure the data into a 2D format where each row
# represents a sensor and each column represents a timestamp.
# #---------------------------
# Question:
# Given a 1D NumPy array, write code to:
# ● Reshape it into a 2D array with an appropriate number of rows and columns.
# ● If the reshaping is not possible due to mismatched elements, explain the error and provide
# a solution by padding/truncating the data.
# Demonstrate the reshaping and necessary checks on a sample array.
#---------------------------
# Answer:
#---------------------------



import numpy as np

# Sample 1D array (e.g., data from sensors over a period of time)
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Dimensions we want to reshape into (rows, columns)
rows = 3  # 3 sensors
cols = 4  # 4 timestamps per sensor

# Check if reshaping is possible (i.e., the total number of elements must match rows * cols)
if data.size == rows * cols:
    reshaped_data = data.reshape((rows, cols))
    print("Reshaped Data:")
    print(reshaped_data)
else:
    print("Reshaping is not possible directly. Adjusting the data...")

    # If reshaping is not possible, we can either truncate or pad the data
    # Option 1: Truncate the data (cut it to the required size)
    truncated_data = data[:rows * cols]
    reshaped_data_truncated = truncated_data.reshape((rows, cols))
    print("Data after truncation:")
    print(reshaped_data_truncated)
    
    # Option 2: Pad the data with zeros (or another value) to match the required size
    padded_data = np.pad(data, (0, rows * cols - data.size), mode='constant')
    reshaped_data_padded = padded_data.reshape((rows, cols))
    print("Data after padding:")
    print(reshaped_data_padded)
