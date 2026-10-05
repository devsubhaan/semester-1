# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter a grade from 0-100: ")

try:
    grade = int(grade)
except ValueError:
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit("Error!")

result = "Fail"

if 70 <= grade <= 100:
    result = "Distinction"
elif 40 <= grade <= 69:
    result = "Pass"

print(f"{grade} is a {result}")
