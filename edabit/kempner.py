# Name: Alexis Raymond
# Date: April 18, 2020
# Exercise: The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero which factorial is exactly divided by the number. (https://edabit.com/challenge/qQnWXBsQaH73yY8r4)

from math import factorial # import the factorial function built into python

##### Method #####
def kempner(n): # returns the smallest integer greater than 0 which factorial is dividable by n
	for i in range(1, n + 1): # iterate through the integers 1 to the number inclusively
		if (factorial(i) % n == 0): # if the factorial of the iterated number divided by the number returns no rest
			return i # return the iterated number

##### Testing #####
print("Test #1: n = 6") # display test label
print(kempner(6)) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: n = 6") # display test label
print(kempner(10)) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: n = 6") # display test label
print(kempner(2)) # display test result
