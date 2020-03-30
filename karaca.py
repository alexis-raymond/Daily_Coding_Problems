# Name: Alexis Raymond
# Date: Mar 30, 2020
# Exercise: Make a function that encrypts a given input with the Karaca encryption algorithm. From https://edabit.com/challenge/JzBLDzrcGCzDjkk5n.

##### Method #####
def karaca(input1): # returns an input encrypted following the Karaca algorithm
	input2 = input1[::-1] # reverse the input

	key = {
		"a": "0",
		"e": "1",
		"o": "2",
		"u": "3"
	} # create the encryption key for the vowells

	input3 = "" # create an empty string that will contain the encrypted input

	for char in input2: # for each character in the input
		if(char in key): # if the character is one of the four vowells in the key
			input3 += key[char] # add the corresponding number to the string

		else: # if the character is not one of the four vowells in the key
			input3 += char # add the character to the string

	return input3 + "aca" # return the encrypted string with the characters a, c and a at the end

##### Testing #####
print("Test #1: banana") # display test label
print(karaca("banana")) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: karaca") # display test label
print(karaca("karaca")) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: burak") # display test label
print(karaca("burak")) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #4: alpaca") # display test label
print(karaca("alpaca")) # display test result