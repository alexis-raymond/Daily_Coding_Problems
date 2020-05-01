# Name: Alexis Raymond
# Date: May 1, 2020
# Exercise: Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string. (https://edabit.com/challenge/g6yjSfTpDkX2STnSX)

##### Method #####
def convertToHex(txt): # return a string with all the hex values of the characters from text
	hex_txt = [] # create an empty list to contain the hex version of the chars

	for char in txt: # iterate through the characters in some text
		hex_txt.append(hex(ord(char))[2:]) # add to the list the hex version of the character

	return " ".join(hex_txt) # return all the hex values separated by a sentence

	# return " ".join(hex(ord(char))[2:] for char in txt) --> one line version

##### Testing #####
print("Test #1: hello world") # display test label
print(convertToHex("hello world")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: Big Boi") # display test label
print(convertToHex("Big Boi")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: Marty Poppinson") # display test label
print(convertToHex("Marty Poppinson")) # display test result