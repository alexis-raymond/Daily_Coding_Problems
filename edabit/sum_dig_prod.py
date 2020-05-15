# Name: Alexis Raymond
# Date: May 15, 2020
# Exercise: Create a function that takes numbers as arguments, adds them together, and returns the product of digits until the answer is only 1 digit long. (https://edabit.com/challenge/HrQoXJYqpYZ2Rqvtb)

##### Method #####
def prod(lst): # returns the product of all the numbers in a list
	prod = 1 # create a variable to hold the product

	for num in lst: # iterate through the numbers in the list
		prod *= int(num) # multiply the product by the iterated number

	return prod # return the product

def sumDigProd(*args): # returns the product of digits of the sum of the numbers until the answer is 1 digit long
	n = sum(args) # create the number variable and initiate it to the sum of all numbers passed as arguments

	while (n >= 10): # while the number is more than 1 digit long
		n = prod(list(str(n))) # change the value of the number to the product of all its digits

	return n # return the number once its 1 digit long

##### Testing #####
print("Test #1: 16, 28") # display test label
print(sumDigProd(16, 28)) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #2: 0") # display test label
print(sumDigProd(0)) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #3: 1, 2, 3, 4, 5, 6") # display test label
print(sumDigProd(1, 2, 3, 4, 5, 6)) # display test result