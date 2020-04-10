# Name: Alexis Raymond
# Date: April 9, 2020
# Exercise: Create a function that takes a variable number of groups of items, and returns the number of ways the items can be arranged, with one item from each group. (https://edabit.com/challenge/G9QRtAGXb9Cu368Pw)

##### Method #####
def combinations(*items): # return the number of possible combinations
	count = 1 # initiate a variable to hold the count
	
	for item in items: # iterate over the items passed as arguments
		if(item > 0): # if the item is greater than 0
			count *= item # multiply the count by the item
	
	return count # return the number of possible combinations

##### Testing #####
print("Test #1: (2,3)") # display test label
print(combinations(2, 3)) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: (3,7,4)") # display test label
print(combinations(3,7,4)) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: (2,3,4,5)") # display test label
print(combinations(2,3,4,5)) # display test result