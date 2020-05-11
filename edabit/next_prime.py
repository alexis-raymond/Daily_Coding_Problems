# Name: Alexis Raymond
# Date: May 11, 2020
# Exercise: Given an integer, create a function that returns the next prime. If the number is prime, return the number itself. (https://edabit.com/challenge/arobBz954ZDxkDC9M)

##### Method #####
def isPrime(num): # returns True if the number is a prime and false otherwise
	for i in range(2, num//2): # iterate through the numbers 2 to half the number
		if (num % i == 0): # if the number divided by the iterated number has no remainder
			return False # return False because it is not prime

	return True # if there are no instances without a remainder, return True because it is prime

def nextPrime(num): # returns the first prime after that number and the number itself if it is a prime
	while (not isPrime(num)): # while the number is not a prime
		num += 1 # go to the next number

	return num # return the number once it is a prime

##### Testing #####
print("Test #1: 12") # display test label
print(nextPrime(12)) # display test result
print("--------\n") # show a line to separate the tests

print("Test #2: 24") # display test label
print(nextPrime(24)) # display test result
print("--------\n") # show a line to separate the tests

print("Test #3: 11") # display test label
print(nextPrime(11)) # display test result