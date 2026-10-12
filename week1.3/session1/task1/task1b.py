# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# Pop gets rid of the end item of a list, pop returns the value removed by default
# so it can get printed

# What features of Python does it rely on?
# It uses a stack as it removes from the right