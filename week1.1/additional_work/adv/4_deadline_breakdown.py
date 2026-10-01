"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

minutes_remaining_input = input("Minutes remaining until the deadline: ")

# Convert the input to an integer
# Extension: detect negative values and print a warning instead
try:
    minutes_remaining_input = int(minutes_remaining_input)
except ValueError:
    print("Invalid input!")

# Calculate whole days, leftover hours, and remaining minutes
days = minutes_remaining_input // 1440
daysExtra = minutes_remaining_input % 1440
hours = minutes_remaining_input // 60
minutesExtra = daysExtra % 60
minutes = minutesExtra

# Print the breakdown using f-strings
print(f"Days: {days}, Hours: {hours}, Minutes: {minutes}")

