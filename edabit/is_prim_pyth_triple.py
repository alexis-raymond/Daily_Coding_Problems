# Name: Alexis Raymond
# Date: May 28, 2020
# Exercise: Create a function that takes a list of three numbers (unordered) and returns True if the numbers constitute a primitive Pythagorean triple, False otherwise. (https://edabit.com/challenge/vLLXeQH5tgyvbzYZS)

##### Method #####
def isPrime(n): # checks if a number is prime
	for i in range(2, n // 2): # iterate through the numbers 2 to half the number
		if (n % i == 0): # if the number divided by the iterated number have no rest
			return False # return false because the number is not prime

	return True # if there are no instances of the division returning no rest, return True, the number is prime

def gcpf(n1, n2): # returns the greatest common prime factor between 2 numbers
	n1_factors, n2_factors = set(), set() # create empty sets for the factors of n1 and n2

	for i in range(1, n1 + 1): # iterate through the numbers 1 and the number inclusively
		if n1 % i == 0: # if the number divided by the iterated number have no rest
			n1_factors.add(i) # add the iterated number to the set of factors

	for i in range(1, n2 + 1): # iterate through the numbers 1 and the number inclusively
		if n2 % i == 0: # if the number divided by the iterated number have no rest
			n2_factors.add(i) # add the iterated number to the set of factors

	common = n1_factors.intersection(n2_factors) # find the common factors between both numbers

	common = set(filter(isPrime, common)) # remove all the common factors that are not prime

	return max(common) # return the highest common prime factor

def isPrimPythTriple(lst): # checks if 3 numbers are primitive Pythagorean triple
	lst.sort() # sort the 3 numbers

	return (lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2) and (gcpf(lst[0], lst[1]) == 1 or gcpf(lst[0], lst[2]) == 1 or gcpf(lst[1], lst[2]) == 1) # returns true if the 3 numbers are primitive pythagorean triples and false otherwise



##### Testing #####
print("Test #1: [4, 5, 3]") # display test label
print(isPrimPythTriple([4, 5, 3])) # display test result
print("--------------------\n") # show a line to separate the tests

print("Test #2: [7, 12, 13]") # display test label
print(isPrimPythTriple([7, 12, 13])) # display test result
print("--------------------\n") # show a line to separate the tests

print("Test #3: [39, 15, 36]") # display test label
print(isPrimPythTriple([39, 15, 36])) # display test result
print("--------------------\n") # show a line to separate the tests

print("Test #4: [77, 36, 85]") # display test label
print(isPrimPythTriple([77, 36, 85])) # display test result