# Name: Alexis Raymond
# Date: May 24, 2020
# Exercise: Write a function that makes the first number as large as possible by swapping out its digits for digits in the second number. (https://edabit.com/challenge/FeNrBCG9rSdNeJTuX)

##### Method #####
def maxPossible(n1, n2): # returns the largest number you can make by swapping digits from 2 numbers
	n1, n2 = map(int, list(str(n1))), map(int, list(str(n2))) # convert the two numbers to lists of their digits

	for i in range(len(n1)): # iterate through the digits in the first number
		if(max(n2) > n1[i]): # if the largest digit from the second number is larger than the iterated digit
			n1[i] = max(n2) # swap the digit of the first number for this value
			n2[n2.index(max(n2))] = 0 # remove the digit from the second number

	return int("".join(map(str, n1))) # return the new number

##### Testing #####
print("Test #1: 9328, 456") # display test label
print(maxPossible(9328, 456)) # display test result
print("-----------------------------\n") # show a line to separate the tests

print("Test #2: 523, 76") # display test label
print(maxPossible(523, 76)) # display test result
print("-----------------------------\n") # show a line to separate the tests

print("Test #3: 9132, 5564") # display test label
print(maxPossible(9132, 5564)) # display test result
print("-----------------------------\n") # show a line to separate the tests

print("Test #4: 8732, 91255") # display test label
print(maxPossible(8732, 91255)) # display test result