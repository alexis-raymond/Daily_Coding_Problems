# Name: Alexis Raymond
# Date: April 13, 2020
# Exercise: Create a function that takes a list and returns a new list containing only prime numbers. (https://edabit.com/challenge/yXZhG7zq6dWhWhirt)

##### Method #####
def isPrimeNumber(x): # returns whether a number is prime or not
	if x >= 2: # if the number is greater than or equal to 2
		for y in range(2,x): # iterate through all integers from 2 to the number (non-inclusive)
			if not (x % y): # if the number divided by the iterated integer has a remainder
				return False # return false (it is not a prime)
	
	else: # if the number is less than 2
		return False # return false
	
	return True # if the number cannot be divided by a smaller integer without a rest, return true (it is a prime)
		
def filterPrimes(num): # returns a filtered list of prime numbers from a list
	return list(filter(isPrimeNumber, num)) # return the filtered list

##### Testing #####
print("Test #1: [7, 9, 3, 9, 10, 11, 27]") # display test label
print(filterPrimes([7, 9, 3, 9, 10, 11, 27])) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: [10007, 1009, 1007, 27, 147, 77, 1001, 70]") # display test label
print(filterPrimes([10007, 1009, 1007, 27, 147, 77, 1001, 70])) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: [1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]") # display test label
print(filterPrimes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097])) # display result of method