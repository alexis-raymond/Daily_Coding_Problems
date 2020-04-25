
# Name: Alexis Raymond
# Date: April 24, 2020
# Exercise: Create a function that takes in n, a, b and returns the number of values raised to the nth power that lie in the range [a, b], inclusive. (https://edabit.com/challenge/abdsaD6gwjgAgevsG)

##### Method #####
def powerRanger(n, a, b): # returns the number of values raised to the nth power that lie in a certain range
	count = 0 # initiate a count variable

	for i in range(a, b + 1): # iterate through the numbers in the specified range (inclusively)
		if ((i ** (1.0 / n)) % 1 == 0): # if the nth root of the iterated number is an integer
			count += 1 # add 1 to the count

	return count # return the count

##### Testing #####
print("Test #1: 2, [49, 65]") # display test label
print(powerRanger(2, 45, 69)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: 3, [1, 27]") # display test label
print(powerRanger(3, 1, 27)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 10, [1, 5]") # display test label
print(powerRanger(10, 1, 5)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: 5, [31, 33]") # display test label
print(powerRanger(5, 31, 33)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #5: 4, [250, 1300]") # display test label
print(powerRanger(4, 250, 1300)) # display test result