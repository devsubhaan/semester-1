# Worksheet 1.3: Task 1
import sys
L = int(input("Length of sequence: ")) # this should be your only input
sequence = []

# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
if not L or L == 0:
    sys.exit("No input!")

for n in range(L-1):
    if n == 0:
        sequence.append(0)
    elif (sequence[n-1]) - n > 0 and n not in sequence:
        sequence.append(sequence[n-1] - n)
    else:
        sequence.append(sequence[n-1] + n)

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence