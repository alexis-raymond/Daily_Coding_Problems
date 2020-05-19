# Name: Alexis Raymond
# Date: May 19, 2020
# Exercise: Create a function that takes a string and applies the Atbash cipher to it. (https://edabit.com/challenge/MGALfBAXhXqqdFyqo)

##### Method #####
def atbash(txt): # returns the atbash encoded version of a string
	alphabet = 'abcdefghijklmnopqrstuvwxyz' # hold all the values of the alphabet

	coded = [] # create an empty list to hold the encoded version of the string

	for char in txt: # iterate through the characters in the string
		if (not char.isalpha()): # if the character is not a letter
			coded.append(char) # add it as is to the encoded list

		else: # if the character is a letter
			coded.append(alphabet[25 - alphabet.find(char)]) if char.islower() else coded.append(alphabet[25 - alphabet.find(char.lower())].upper()) # add its mirror to the encoded list while keeping the case

	return ''.join(coded) # return a string verison of the encoded list of characters

##### Testing #####
print("Test #1: apple") # display test label
print(atbash('apple')) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: Hello world!") # display test label
print(atbash('Hello world!')) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: Christmas is the 25th of December") # display test label
print(atbash('Christmas is the 25th of December')) # display test result
print("--------------------------------------------\n") # show a line to separate the tests