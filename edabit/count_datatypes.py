# Name: Alexis Raymond
# Date: April 29, 2020
# Exercise: Given a function that accepts unlimited arguments. Check and count how many data types are in those arguments. Finally return the total in a list. List order is [int, str, bool, list, tuple, dictionary] (https://edabit.com/challenge/HXkpnCxJgxkFwaReT)

##### Method #####
def countDataTypes(*args): # returns the count for each data type in the arguments
	types = [0, 0, 0, 0, 0, 0] # create a list to record the counts for each datatype

	for arg in args: # iterate through all the arguments provided
		if (type(arg) == int): # if the argument is an int
			types[0] += 1 # add 1 to its count

		elif (type(arg) == str): # if the argument is a string
			types[1] += 1 # add 1 to its count

		elif (type(arg) == bool): # if the argument is a boolean
			types[2] += 1 # add 1 to its count

		elif (type(arg) == list): # if the argument is a list
			types[3] += 1 # add 1 to its count

		elif (type(arg) == tuple): # if the argument is a tuple
			types[4] += 1 # add 1 to its count

		elif (type(arg) == dict): # if the argument is a dictionary
			types[5] += 1 # add 1 to its count

	return types # return the list with the counts for each type

##### Testing #####
print("Test #1: [1, 45, Hi, False]") # display test label
print(countDataTypes(1, 45, "Hi", False)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: [[10, 20], (t, Ok), 2, 3, 1]") # display test label
print(countDataTypes([10, 20], ("t", "Ok"), 2, 3, 1)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: [Hello, Bye, True, True, False, {'1': 'One', '2': 'Two'}, [1, 3], {'Brayan': 18}, 25, 23]") # display test label
print(countDataTypes("Hello", "Bye", True, True, False, {'1': 'One', '2': 'Two'}, [1, 3], {'Brayan': 18}, 25, 23)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: [4, 21, (ES, EN), ('a', 'b'), False, [1, 2, 3], [4, 5, 6]]") # display test label
print(countDataTypes(4, 21, ("ES", "EN"), ('a', 'b'), False, [1, 2, 3], [4, 5, 6])) # display test result