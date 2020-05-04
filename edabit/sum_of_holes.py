# Name: Alexis Raymond
# Date: May 4, 2020
# Exercise: Your task is to create a function with argument N that returns the sum of the holes for the integers n in the range of range 0 < n <= N. (https://edabit.com/challenge/2tkcbQgPJZPPpzg2i)

##### Method #####
def sumOfHoles(N): # returns the number of holes in the range 0 < n <= N
	holes = {
		"0": 1,
		"1": 0,
		"2": 0,
		"3": 0,
		"4": 1,
		"5": 0,
		"6": 1,
		"7": 0,
		"8": 2,
		"9": 1
	} # create a dictionary that holds the number of holes in all 10 digits

	hole_count = 0 # create a variable to hold the count of holes

	for i in range(1, N + 1): # iterate through the numbers from 1 to N inclusively
		for digit in str(i): # iterate through the digits in the iterated number
			hole_count += holes[digit] # add the number of holes in the iterated number to the count

	return hole_count # return the total count

##### Testing #####
print("Test #1: 4") # display test label
print(sumOfHoles(4)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: 6") # display test label
print(sumOfHoles(6)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 8") # display test label
print(sumOfHoles(8)) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: 6259") # display test label
print(sumOfHoles(6259)) # display test result