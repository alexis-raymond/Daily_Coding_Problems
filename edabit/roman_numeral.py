# Name: Alexis Raymond
# Date: May 21, 2020
# Exercise: Create a function that takes in a Roman numeral as a string and converts it to an integer, returning the result. (https://edabit.com/challenge/oepiudBYC7PT7TXAM)

##### Method #####
def parseRomanNumeral(num): # returns the integer value of a roman numeral
	notation = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	} # create a dictionary with the value of each roman letter

	numerics = list(map(lambda char: notation[char], list(num))) # create a list with the integer value of each letter
	number = 0 # create a variable to hold the final number
	i = 0 # create a variable to iterate through the numbers in the list

	while (i < len(numerics)): # iterate through all the numbers in the list
		if (i == len(numerics) - 1): # if the iterated number is the last one
			number += numerics[i] # add it to the running total

		elif (numerics[i] >= numerics[i+1]): # if the iterated number is greater than or equal to the next number in the list
			number += numerics[i] # add it to the running total

		else: # if the iterated number is less than the next number in the list
			number += numerics[i+1] - numerics[i] # add the difference between the next number and the iterated number to the running total
			i += 1 # skip the next number in the iteration

		i += 1 # iterate to the next number

	return number # return the running total

##### Testing #####
print("Test #1: VII") # display test label
print(parseRomanNumeral('VII')) # display test result
print("-----------------------\n") # show a line to separate the tests

print("Test #2: DCLXXIX") # display test label
print(parseRomanNumeral('DCLXXIX')) # display test result
print("-----------------------\n") # show a line to separate the tests

print("Test #3: MMMCMV") # display test label
print(parseRomanNumeral('MMMCMV')) # display test result