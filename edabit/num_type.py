# Name: Alexis Raymond
# Date: April 28, 2020
# Exercise: Create a function that takes a number and returns "Perfect" if the number is perfect, "Amicable" if the number is part of an amicable pair, or "Neither". (https://edabit.com/challenge/9cNxcMjfEMzKYoBZY)

##### Method #####
def numType(n): # returns whether the number is perfect, amicable or neither
	x_divisors = [] # create a list to hold the divisors of n

	for i in range(1, n // 2 + 1): # iterate through the numbers 1 to the half of n (inclusively)
		if (n % i == 0): # if i is a divisor of n
			x_divisors.append(i) # add i to the list of divisors

	if (sum(x_divisors) == n): # if the sum of all the divisors is n
		return "Perfect" # return "Perfect"

	y_divisors = [] # create a list to hold the divisors of y (y = sum of all divisors of n)

	for i in range(1, sum(x_divisors) // 2 + 1): # iterate through the numbers 1 to the half of y (inclusively)
		if (sum(x_divisors) % i == 0): # if i is a divisor of y
			y_divisors.append(i) # add i to the list of divisors

	if (sum(y_divisors) == n): # if the sum of all the divisors of y is n
		return "Amicable" # return "Amicable"

	return "Neither" # if the number is neither perfect or amicable, return "Neither"

##### Testing #####
print("Test #1: 6") # display test label
print(numType(6)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: 2924") # display test label
print(numType(2924)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 5010") # display test label
print(numType(5010)) # display test result