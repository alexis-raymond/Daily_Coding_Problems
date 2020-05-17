# Name: Alexis Raymond
# Date: May 16, 2020
# Exercise: Create a function that takes the dimensions of two triangles (as lists) and checks if the first triangle fits into the second one. (https://edabit.com/challenge/dRA9E9HxJdbuB4yCx)

##### Method #####
def doesTriangleFit(brick, hole): # returns whether two triangles are possible and if the first can fit in the other
	if ((brick[0] + brick[1] <= brick[2]) or (brick[0] + brick[2] <= brick[1]) or (brick[1] + brick[2] <= brick[0]) or (hole[0] + hole[1] <= hole[2]) or (hole[0] + hole[2] <= hole[1]) or (hole[1] + hole[2] <= hole[0])): # use triangle inequality theorem to assess whether both triangles are possible
		return False # if one triangle is not possible return false

	p_brick, p_hole = sum(brick)/2, sum(hole)/2 # calculate the half perimeter of each triangle (used to calculate their areas)

	return p_brick * (p_brick - brick[0]) * (p_brick - brick[1]) * (p_brick - brick[2]) <= p_hole * (p_hole - hole[0]) * (p_hole - hole[1]) * (p_hole - hole[2]) # return whether the first area is smaller than the second

##### Testing #####
print("Test #1: [1, 1, 1], [1, 1, 1]") # display test label
print(doesTriangleFit([1, 1, 1], [1, 1, 1])) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #2: [1, 1, 1], [2, 2, 2]") # display test label
print(doesTriangleFit([1, 1, 1], [2, 2, 2])) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #3: [1, 2, 3], [1, 2, 2]") # display test label
print(doesTriangleFit([1, 2, 3], [1, 2, 2])) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #4: [1, 2, 4], [1, 2, 6]") # display test label
print(doesTriangleFit([1, 2, 4], [1, 2, 6])) # display test result