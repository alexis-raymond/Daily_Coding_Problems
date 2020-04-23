# Name: Alexis Raymond
# Date: April 23, 2020
# Exercise: Write the function that takes three dimensions of a brick: height(a), width(b) and depth(c) and returns True if this brick can fit into a hole with the width(w) and height(h). (https://edabit.com/challenge/EyzmkffNRiEBtjAmf)

##### Method #####
def doesBrickFit(a,b,c,w,h): # returns whether a brick can fit through a hole
	if ((a <= h) and (b <= w)): # if you can fit the brick through its width and height
		return True

	if ((a <= h) and (c <= w)): # if you can fit the brick through its height and depth
		return True

	if ((b <= w) and (c <= h)): # if you can fit the brick through its width and depth
		return True

	if ((a <= w) and (b <= h)): # if you can fit the brick through its width and height (reversed)
		return True

	if ((a <= w) and (c <= h)): # if you can fit the brick through its height and depth (reversed)
		return True

	if ((b <= h) and (c <= w)): # if you can fit the brick through its width and depth (reversed)
		return True

	return False # if all the possible sides of the brick cannot fit, return false

##### Testing #####
print("Test #1: 1, 1, 1, 1, 1") # display test label
print(doesBrickFit(1, 1, 1, 1, 1)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: 1, 2, 1, 1, 1") # display test label
print(doesBrickFit(1, 2, 1, 1, 1)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 1, 2, 2, 1, 1") # display test label
print(doesBrickFit(1, 2, 2, 1, 1)) # display test result