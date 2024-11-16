# Scenario: You are working on a function that processes a list of values by dividing each by a
# divisor provided by the user. If the divisor is zero, an error occurs. If the divisor is a non-integer
# or non-numeric type, it should also raise an error.
#---------------------------
# Question:
# Write a function divide_elements(values, divisor) that accepts a list of numbers and a divisor.
# Use built-in exception handling to catch a ZeroDivisionError when dividing by zero and a
# TypeError if the divisor is not numeric. Ensure the program provides meaningful error messages
# to the user and gracefully continues processing if possible.
#---------------------------
# Answer:
#---------------------------

def divide_elements(values, divisor):
    try:
        # Check if the divisor is numeric
        if not isinstance(divisor, (int, float)):
            raise TypeError("The divisor must be a numeric value.")

        # Perform division and handle ZeroDivisionError
        results = [value / divisor for value in values]
        return results

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Test cases
values_list = [10, 20, 30, 40, 50]

print("Case 1: Valid divisor")
print(divide_elements(values_list, 10))  # Should return valid results

print("\nCase 2: Zero divisor")
print(divide_elements(values_list, 0))  # Should handle division by zero

print("\nCase 3: Non-numeric divisor")
print(divide_elements(values_list, "abc"))  # Should handle non-numeric divisor
