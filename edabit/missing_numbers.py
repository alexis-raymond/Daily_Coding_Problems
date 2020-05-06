# Name: Alexis Raymond
# Date: May 6, 2020
# Exercise: Create a function that takes a list of "mostly" numbers, counts the amount of missing numbers and returns their sum. (https://edabit.com/challenge/vBwRuR4mF5yQ4cNuc)

##### Method #####
def missingNumbers(lst): # returns the number of missing numbers in the sequence
	lst = sorted(map(int, filter(lambda a: a.isdigit(), lst))) # sort the list, convert all items to numbers, and remove items that are not numbers

	count = 0 # create a variable to hold the count of missing numbers

	for i in range(len(lst) - 1): # iterate through the indices of the list
		count += lst[i + 1] - lst[i] - 1 # add the difference between each number to the count

	return count # return the count of missing numbers

##### Testing #####
print('Test #1: ["1", "3", "5", "7", "9"]') # display test label
print(missingNumbers(["1", "3", "5", "7", "9"])) # display test result
print("---------------\n") # show a line to separate the tests

print('Test #2: ["7", "3", "1", "9", "5"]') # display test label
print(missingNumbers(["7", "3", "1", "9", "5"])) # display test result
print("---------------\n") # show a line to separate the tests

print('Test #3: ["1", "5", "B", "9", "z"]') # display test label
print(missingNumbers(["1", "5", "B", "9", "z"])) # display test result