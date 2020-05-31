# Name: Alexis Raymond
# Date: May 31, 2020
# Exercise: You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. (problem 100 of newsletter)

##### Method #####
def stepsToPoint(points): # returns the minimum number of steps to follow the point sequence
	steps = 0 # initiate a variable to hold the number of steps

	for i in range(len(points) - 1): # iterate through the points
		steps += max(abs(points[i + 1][0] - points[i][0]), abs(points[i + 1][1] - points[i][1])) # add the minimum number of steps needed to go from the iterated point to the next one

	return steps # return the total number of steps

	# return sum([max(abs(points[i + 1][0] - points[i][0]), abs(points[i + 1][1] - points[i][1])) for i in range(len(points) -1)]) # one line function

##### Testing #####
print("Test #1: [(0, 0), (1, 1), (1, 2)] -> 2") # display test label
print(stepsToPoint([(0, 0), (1, 1), (1, 2)])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: [(1,2), (4,-1), (0,0), (1,1)] -> 8") # display test label
print(stepsToPoint([(1,2), (4,-1), (0,0), (1,1)])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: [(100,200), (50,75), (0,0)] -> 200") # display test label
print(stepsToPoint([(100,200), (50,75), (0,0)])) # display test result