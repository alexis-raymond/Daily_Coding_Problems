# Name: Alexis Raymond
# Date: April 20, 2020
# Exercise: A Primorial is a product of the first n prime numbers. Create a function that returns the Primorial of a number. (https://edabit.com/challenge/fRjfrCYXWJAaQqFXF)

##### Method #####
def isPrime(n): # returns True if the number is prime and false otherwise
	for i in range(2,n): # iterate through all the numbers between 2 and n exclusively
		if (n % i == 0): # if there is no rest after dividing n by the iterated number
			return False # return false (the number is not a prime)

	return True # if there are no numbers that return no rest, return true (the number is a prime)

def primorial(n): # returns the primorial of a number
	product = 1 # initiate a variable to hold the product
	i = 2 # initiate a variable to hold the numbers we are going to iterate through (this is going to be used to find n primes)

	while (n > 0): # while we have not find n prime numbers
		if(isPrime(i)): # if the iterated number is prime
			product *= i # multiply it to the product
			n -= 1 # substract 1 from the number of primes to find

		i += 1 # add 1 to the number we are using to find primes

	return product # return the product

##### Testing #####
print("Test #1: 1") # display test label
print(primorial(1)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: 2") # display test label
print(primorial(2)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 8") # display test label
print(primorial(8)) # display test result