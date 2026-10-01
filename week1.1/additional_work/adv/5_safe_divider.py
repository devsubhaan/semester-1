"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""

numerator_input = input("Enter the numerator: ")
denominator_input = input("Enter the denominator: ")

# Wrap the risky operations in a try/except block
# Convert the values to integers and perform the division
try:
    numerator_input = int(numerator_input)
    denominator_input = int(denominator_input)
except ValueError:
    print("Invalid inputs!")

# Print clear feedback when something goes wrong
try:
    result = numerator_input / denominator_input
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # Only show the answer when the division succeeds
    print(f"Result: {result}")

