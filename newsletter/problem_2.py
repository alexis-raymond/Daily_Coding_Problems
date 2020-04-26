# Name: Alexis Raymond
# Date: Feb 19, 2020
# Exercise: given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i (daily coding problem 2)


##### Method (with division) #####
def arrayProductDiv(listOfInt): # returns the array with each number multiplied by the product of the array except the term at index i
	product = 1 # create a variable to hold the array's product
	newList = [] # create an empty list to hold the result of the method

	for num in listOfInt: # loop through the numbers in the array
		product *= num # multiply each number of the array together to hold the product

	for num in listOfInt: # loop through the numbers in the array
		newList.append(product // num) # add the product of the array divided by the number to a new list

	return newList # return the new list

##### Method (without division) #####
def arrayProductNoDiv(listOfInt):
	newList = [] # create an empty list to hold the result of the method

	for i in range(len(listOfInt)): # loop through the numbers in the array
		num = 1 # create a variable to hold the new number

		for x in range(len(listOfInt)): # loop through the numbers in the array
			if(i != x): # if the indexes are different, multiply the number with the product
				num *= listOfInt[x]

		newList.append(num) # add the new number to the result list

	return newList # return the new list

##### Testing both methods #####
print("Test #1 (answer = [120,60,40,30,24])") # display test label
print("Without division:", arrayProductNoDiv([1,2,3,4,5])) # test without division
print("With division:", arrayProductDiv([1,2,3,4,5])) # test with division
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2 (answer = [2,3,6])") # display test label
print("Without division:", arrayProductNoDiv([3,2,1])) # test without division
print("With division:", arrayProductDiv([3,2,1])) # test with division
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3 (answer = [8,5])") # display test label
print("Without division:", arrayProductNoDiv([5,8])) # test without division
print("With division:", arrayProductDiv([5,8])) # test with division
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4 (answer = [23040,11520,7680,5760,4608,3840])") # display test label
print("Without division:", arrayProductNoDiv([2,4,6,8,10,12])) # test without division
print("With division:", arrayProductDiv([2,4,6,8,10,12])) # test with division