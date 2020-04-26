# Name: Alexis Raymond
# Date: April 26, 2020
# Exercise: Create a function that takes an array of three numbers and returns the Least Common Multiple (LCM). (https://edabit.com/challenge/7kZhB4FpJfYHnQYBq)

##### Method #####
def lcmThree(num): # returns the least common multiple of three numbers
	i = 1 # create an iterator to find the multiples of the largest of the three numbers

	while not(((max(num) * i % num[0] == 0) & (max(num) * i % num[1] == 0) & (max(num) * i % num[2] == 0))): # while the iterated multiple of the largest number is not a multiple of all three numbers
		i += 1 # add 1 to the iterator

	return max(num) * i # return the last iterated multiple of the largest of the three numbers 

##### Testing #####
print("Test #1: 5 - 7 - 13") # display test label
print(lcmThree([5, 7, 13])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: 104 - 105 - 107") # display test label
print(lcmThree([104, 105, 107])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 19 - 47 - 43") # display test label
print(lcmThree([19, 47, 43])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests
