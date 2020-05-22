# Name: Alexis Raymond
# Date: May 22, 2020
# Exercise: Create a function that returns the simplified version of a fraction. (https://edabit.com/challenge/vQgmyjcjMoMu9YGGW)

##### Method #####
def gcd(num1, num2): # returns the greater common divisor between 2 numbers
	for i in range(max(num1, num2) // 2, 0, -1): # iterate through the numbers half the biggest number to 1
		if (num1 % i == 0 and num2 % i == 0): # if the iterated number is a divisor of both numbers
			return i # return the iterated number

def simplify(txt): # returns the simplified version of a fraction
	num1, num2 = int(txt.split("/")[0]), int(txt.split("/")[1]) # create variables for both numbers

	if (num1 % num2 == 0): # if num1 is dividable by num2
		return str(num1 // num2) # return the quotient of both numbers

	return str(num1 // gcd(num1, num2)) + "/" + str(num2 // gcd(num1, num2)) # return the fraction simplified using the greater common divisor

##### Testing #####
print("Test #1: 4/6") # display test label
print(simplify("4/6")) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #2: 10/11") # display test label
print(simplify("10/11")) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #3: 100/400") # display test label
print(simplify("100/400")) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #4: 8/4") # display test label
print(simplify("8/4")) # display test result
print("-----------------\n") # show a line to separate the tests