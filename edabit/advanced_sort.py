# Name: Alexis Raymond
# Date: May 20, 2020
# Exercise: Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist. (https://edabit.com/challenge/6vSZmN66xhMRDX8YT)

##### Method #####
def advancedSort(lst): # returns the list sorted in sublists containing all identical elements
	sort_lst = [] # create an empty list to contain the sorted list

	for item in set(lst): # for each item in the list (no duplicates)
		sort_lst.append([item for i in range(lst.count(item))]) # add to the sorted list a list containing the item

	return sorted(sort_lst, key = lambda l: lst.index(l[0])) # return the list of sublists sorted in function of their position in the initial list

	# return [[item for i in range(lst.count(item))] for item in sorted(set(lst), key = lst.index)] # one line function

##### Testing #####
print("Test #1: [2, 1, 2, 1]") # display test label
print(advancedSort([2, 1, 2, 1])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: [5, 4, 5, 5, 4, 3]") # display test label
print(advancedSort([5, 4, 5, 5, 4, 3])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print('Test #3: ["b", "a", "b", "a", "c"]') # display test label
print(advancedSort(["b", "a", "b", "a", "c"])) # display test result