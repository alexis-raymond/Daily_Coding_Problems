# Name: Alexis Raymond
# Date: May 13, 2020
# Exercise: Given three groups of numbers, return a list containing all numbers that appear in more than one group (in ascending order). (https://edabit.com/challenge/SYmHGXX2P26xu7JFR)

##### Method #####
def numberGroups(group1, group2, group3): # returns a sorted list of the numbers that appear in more than 1 group
	duplicates = set() # create a new set to contain the duplicate numbers

	for num in group1: # iterate through the numbers in the first group
		if (num in group2 + group3): # if the iterated number is also in group2 or 3
			duplicates.add(num) # add it to the set of duplicates

	for num in group2: # iterate through the numbers in the second group
		if (num in group3): # if the iterated number is also in group3
			duplicates.add(num) # add it to the set of duplicates

	return sorted(list(duplicates)) # return the set converted to a list and sorted

##### Testing #####
print("Test 1: [7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]") # display test label
print(numberGroups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5])) # display result of method
print("---------------------------\n") # show a line to separate the tests

print("Test 2: [3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]") # display test label
print(numberGroups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3])) # display result of method
print("---------------------------\n") # show a line to separate the tests

print("Test 3: [4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2]") # display test label
print(numberGroups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2])) # display result of method
print("---------------------------\n") # show a line to separate the tests

print("Test 4: [7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6]") # display test label
print(numberGroups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6])) # display result of method