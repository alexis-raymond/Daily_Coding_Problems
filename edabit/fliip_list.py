# Name: Alexis Raymond
# Date: April 27, 2020
# Exercise: Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list. (https://edabit.com/challenge/QoavwQhmrDpXJhBW9)

##### Method #####
def flipList(lst): # returns the flipped version of the list
	flipped = [] # create an empty list to contain the flipped list

	for item in lst: # iterate through the items in the list
		if (isinstance(item, list)): # if the item is a list
			flipped.append(item[0]) # add the item inside the list to the flipped list

		else: # if the item is not a list
			flipped.append([item]) # add the item to the flipped list as a list

	return flipped # return the flipped list

##### Testing #####
print("Test #1: [1, 2, 3, 4]") # display test label
print(flipList([1, 2, 3, 4])) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests	

print("Test #1: [[5], [6], [9]]") # display test label
print(flipList([[5], [6], [9]])) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests	

print("Test #1: []") # display test label
print(flipList([])) # display result of method