"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = input("Travel cost in pounds: ")
food_cost_input = input("Food cost in pounds: ")
accommodation_cost_input = input("Accommodation cost in pounds: ")

# Convert each value to a number type that supports decimals
try:
    travel_cost_input = float(travel_cost_input)
    food_cost_input = float(food_cost_input)
    accommodation_cost_input = float(accommodation_cost_input)
except ValueError:
    print("One or more inputs are not valid floats!")

# Calculate the total and the average spend per category
total_cost = travel_cost_input + food_cost_input + accommodation_cost_input

# Print the three costs, the total, and the average
average_values = total_cost / 3
print(f"Average: {average_values:.2f}")
print(f"Travel: {travel_cost_input:.2f}, Food: {food_cost_input:.2f}, Accommodation: {accommodation_cost_input:.2f}")
# Extension: format the totals to two decimal places
