# Worksheet 1.3: Task 3
import os
import sys
# Your code for the overall grade classification
# ask for filename of the student file
filename = input("What is the file name (csv) of the student file? ")
if not os.path.exists(filename):
    sys.exit("Invalid file, make sure to add .csv at the end!")

# open the file
with open(filename) as f:
    # read in the data, and for each student calculate their average grade and classification
    col = f.readline()
    while f.readline():
        print(f.readline())

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder