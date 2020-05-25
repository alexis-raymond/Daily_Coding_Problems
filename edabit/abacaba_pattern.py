# Name: Alexis Raymond
# Date: May 25, 2020
# Exercise: Create a function that takes a number n as an argument and returns a string that represents the full pattern. (https://edabit.com/challenge/FDzEFbNE2q3eKL8dm)

##### Method #####
def abacabaPattern(n): # returns the abacaba pattern at the specified order
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # create a variable holding the alphabet

	# return "A" if n == 1 else abacabaPattern(n-1) + alpha[n-1] + abacabaPattern(n-1) # one line statement

	if (n == 1): # if n is 1
		return "A" # return only the letter A

	else: # if n is greater than 1
		return abacabaPattern(n-1) + alpha[n-1] + abacabaPattern(n-1) # return the pattern for n-1 twice with the next letter in between

##### Testing #####
for i in range(1, 6): # iterate through the numbers 1 to 5 inclusively
	print("Test " + str(i)) # print the test label
	
	print(abacabaPattern(i)) # print the display label

	print("----------------------------------\n") # show a line to separate the tests
