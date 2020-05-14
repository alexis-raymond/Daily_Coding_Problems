# Name: Alexis Raymond
# Date: May 14, 2020
# Exercise: Create two functions that take an integer as an argument and return its additive persistence and multiplicative persistence. (https://edabit.com/challenge/5ou6SKDtFRZugbpda)

##### Method #####
def prod(lst): # returns the product of all the numbers in a list
	product = 1 # create a variable to hold the product

	for item in lst: # iterate through the numbers in the list
		product *= item # multiply the product by the iterated number

	return product # return the product

def additivePersistence(n): # returns the number of times you have to replace a number by the sum of its digits for it to have only one digit
	count = 0 # create a count variable

	while (n >= 10): # while there is more than 1 digit
		n = sum(list(map(int, list(str(n))))) # replace n by the sum of its digits
		count += 1 # add 1 to the count

	return count # once the number is only 1 digit long, return the count

def multiplicativePersistence(n): # returns the number of times you have to replace a number by the product of its digits for it to have only one digit
	count = 0 # create a count variable

	while (n >= 10): # while there is more than 1 digit
		n = prod(list(map(int, list(str(n))))) # replace n by the product of its digits
		count += 1 # add 1 to the count

	return count # once the number is only 1 digit long, return the count

##### Testing #####
print("########## Additive Persistence ##########")
print("Test #1: 1679583") # display test label
print(additivePersistence(1679583)) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #2: 123456") # display test label
print(additivePersistence(123456)) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #3: 6") # display test label
print(additivePersistence(6)) # display test result
print("-----------------\n") # show a line to separate the tests

print("########## Multiplicative Persistence ##########")
print("Test #1: 77") # display test label
print(multiplicativePersistence(77)) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #2: 123456") # display test label
print(multiplicativePersistence(123456)) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #3: 4") # display test label
print(multiplicativePersistence(4)) # display test result