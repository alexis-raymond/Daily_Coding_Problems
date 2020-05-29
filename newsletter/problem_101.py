# Name: Alexis Raymond
# Date: May 29, 2020
# Exercise: Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number. (daily coding problem 101)


##### Method #####
def isPrime(n): # checks if a number is prime
	for i in range(2, n // 2): # iterate through the numbers 2 and half the number
		if (n % i == 0): # if there are no rest when you divide the number by the iterated number
			return False # the number is not prime

	return True # if there are no numbers that you can divide the initial number by without having a rest, the number is prime

def sumTwoPrimes(n): # returns two prime numbers whose sum is the number
	for i in range(3, n): # iterate through the numbers 3 and n exclusively
		if (isPrime(i) and isPrime(n - i)): # if the iterated number and n minus the iterated number are prime
			return i, n - i # return the pair of numbers

##### Testing both methods #####
print("Test #1: 6") # display test label
print(sumTwoPrimes(6)) # test without division
print("------------------\n") # show a line to separate the tests

print("Test #2: 10") # display test label
print(sumTwoPrimes(10)) # test without division
print("------------------\n") # show a line to separate the tests

print("Test #3: 100") # display test label
print(sumTwoPrimes(100)) # test without division