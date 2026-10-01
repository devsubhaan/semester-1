"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = input("How many miles will you travel? ")
time_hours_input = input("How many hours will the journey take? ")

# Convert distance_miles_input and time_hours_input to numbers
# Validation for zero or negative values

try:
    distance_miles_input = int(distance_miles_input)
    time_hours_input = int(time_hours_input)
except ValueError:
    print("Invalid entries for either distance or time!")

if distance_miles_input <= 0:
    print("Distance must be positive!")
elif time_hours_input <= 0:
    print("Time must be positive")
else:
    # Calculate the average speed in miles per hour
    average_speed = distance_miles_input / time_hours_input

    # Print a summary message using an f-string
    print(f"Destination: {destination}, Speed: {average_speed:.2f}")




