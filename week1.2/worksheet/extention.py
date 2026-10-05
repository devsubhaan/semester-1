# Worksheet 1.2: Task 2 Solution
import sys
from util import read_file, standard_deviation

filename = sys.argv[1]
float_list = read_file(filename)

if not float_list:
    sys.exit("No numbers entered!")

print(f"Minimum = {min(float_list)}")
print(f"Maximum =  {max(float_list)}")
print(f"Mean = {sum(float_list) / len(float_list)}")
sorted_list = sorted(float_list)
print(f"Median = {sorted_list[len(float_list) // 2]}")
print(f"Standard Deviation = {standard_deviation(float_list)}")
