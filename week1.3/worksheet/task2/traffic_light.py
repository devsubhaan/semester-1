"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input(""))  # read an integer number of steps (>0)

state = "red"
count = 0

# Simulate the traffic light system up to time=maxtime in 1-second steps
while count < maxtime:
    for colour, item in states.items():
        for i in range(item):
            print(f"Time {systime:03} State {colour}")
            systime += 1
            count += 1
            if count == maxtime+1:
                break
        if count == maxtime+1:
            break
