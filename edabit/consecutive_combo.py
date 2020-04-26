# Name: Alexis Raymond
# Date: April 9, 2020
# Exercise: Write a function that returns True if two lists, when combined, form a consecutive sequence. (https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb)

##### Method #####
def consecutive_combo(lst1, lst2): # return true if the two lists combined formed a consecutive sequence
	lst3 = lst1 + lst2 # merge the 2 lists

	lst3.sort() # sort the merged list

	for i in range(len(lst3) - 1): # iterate through all the terms in the list except the last one
		if(lst3[i] + 1 != lst3[i + 1]): # if the iterated term + 1 is not equal to the next term in the list, return false
			return False

	return True # if all the terms in the merged list are consecutive, return true

##### Testing #####
print("Test #1: [7, 4, 5, 1], [2, 3, 6]") # display test label
print(consecutive_combo([7, 4, 5, 1], [2, 3, 6])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: [1, 4, 6, 5], [2, 7, 8, 9]") # display test label
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: [1, 4, 5, 6], [2, 3, 7, 8, 10]") # display test label
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #4: [44, 46], [45]") # display test label
print(consecutive_combo([44, 46], [45])) # display test result
