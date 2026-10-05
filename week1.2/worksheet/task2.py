# Worksheet 1.2: Extention Solution
import sys
from util import read_numbers

float_list = read_numbers()
if not float_list:
    sys.exit("Error: no numbers provided")

print(f"Minimum = {min(float_list)}")
print(f"Maximum = {max(float_list)}")
print(f"Mean = {sum(float_list) / len(float_list)}")
sorted_list = sorted(float_list)
print(f"Median = {sorted_list[len(float_list) // 2]}")
