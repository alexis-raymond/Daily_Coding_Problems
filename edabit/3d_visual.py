# Name: Alexis Raymond
# Date: April 21, 2020
# Exercise: Create a function that takes a number (step) as an argument and returns the amount of blocks in that step. (https://edabit.com/challenge/NtsqbRPqtPYhR8tJe)

##### Method #####
def blocks(step): # return the number of blocks in the sequence at the specified number of steps
	if (step == 0): # if there are 0 steps
		return 0 # return 0
	
	if (step == 1): # if there is 1 step
		return 5 # return 5
	
	return 5 + step + blocks(step - 1) # return 5 new blocks + number of steps + the total blocks in the sequence with one less step

##### Testing #####
for i in range(1, 6): # iterate through the numbers 1 to 5 inclusively
	print("Test " + str(i)) # print the test label
	print(blocks(i)) # display test result
	print("-------------------------\n") # show a line to separate the tests
