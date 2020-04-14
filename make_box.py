# Name: Alexis Raymond
# Date: April 14, 2020
# Exercise: Create a function that creates a box based on dimension n. (https://edabit.com/challenge/dy3WWJr34gSGRPLee)

##### Method #####
def makeBox(n): # return a square box with the sides of length n
	if(n == 1): # if the dimension is 1
		return ["#"] # return just 1 #

	box = [] # create an empty list to hold the box

	box.append("#" * n) # add the first line full of # to the list

	for i in range(n-2): # iterate through n-2 lines for the middle of the box
		box.append("#" + " " * (n-2) + "#") # add the middle lines (empty in the inside) to the list

	box.append("#" * n) # add the last line full of # to the list

	return box # return the list with all the lines

##### Testing #####
for i in range(1, 6): # iterate through the numbers 1 to 5 inclusively
	print("Test " + str(i)) # print the test label
	
	for line in makeBox(i): # iterate through the lines in the box
		print(line) # print the line

	print("-------------------------\n") # show a line to separate the tests