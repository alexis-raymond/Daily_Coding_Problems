# Name: Alexis Raymond
# Date: April 21, 2020
# Exercise: Create a function that takes a number (step) as an argument and returns the amount of blocks in that step. (https://edabit.com/challenge/NtsqbRPqtPYhR8tJe)

##### Method #####
import math # import math function

def cannon(location, angle, distance): # returns the location of a bullet shot from a cannon
	location = list(location) # convert the location to a list so we can change the values

	location[0] += round(distance * math.sin(math.radians(angle))) # add the horizontal value of the triangle to the x coordinate
	location[1] += round(distance * math.cos(math.radians(angle))) # add the vertical value of the triangle to the y coordinate

	return tuple(location) # return a tuple version of the coordinates of the bullet

##### Testing #####
print("Test #1: (0,0),0,10") # display test label
print(cannon((0,0),0,10)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: (0,0),270,10") # display test label
print(cannon((0,0),270,10)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: (0,0),45,10") # display test label
print(cannon((0,0),45,10)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: (-12,-2),193,9") # display test label
print(cannon((-12,-2),193,9)) # display test result