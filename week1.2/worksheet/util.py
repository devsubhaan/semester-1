"""
Utility functions for Worksheet 1.2.
"""


def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers

def read_file(filename):
    file = open(filename)
    data = file.read()
    numbers = [float(item) for item in data.split()]
    return numbers

def standard_deviation(values):

    mean = sum(values) / len(values)
    squared_deviations = [(val - mean) ** 2 for val in values]
    variance = sum(squared_deviations) / len(values)
    std = variance ** 0.5
    return std
