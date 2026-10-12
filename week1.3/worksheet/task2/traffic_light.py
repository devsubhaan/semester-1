"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"



# Simulate the traffic light system up to time=maxtime in 1-second steps
for colour, time in states.items():
    for i in range(time):
        print(f"Time {systime:03} State {colour}")
        systime +=1
        if systime > maxtime:
            break
    if systime > maxtime:
        break    
# At the end of each step you should output the time and state using the statement on line 14