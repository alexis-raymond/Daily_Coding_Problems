# Name: Alexis Raymond
# Date: Mar 15, 2020
# Exercise: Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

##### Method #####
def balanced(expression): # returns whether the list of characters is balanced or not
	opposites = {
		"[": "]",
		"(": ")",
		"{": "}"
	} # create a dictionary with the closing character for each opener

	open_chars = [] # create an empty list to hold the opened characters

	for char in expression: # iterate through the characters in the list
		if(len(open_chars) == 0): # if there aren't any open characters
			open_chars.append(char) # add the current character to the list of open characters

		elif((open_chars[-1] in opposites) and (char == opposites[open_chars[-1]])): # if the current character is the closing character of the last opened character
			open_chars.pop() # remove the opened character from the list

		else: # if the current character is not the closing character of the last opened character
			open_chars.append(char) # add the current character to the list

	return len(open_chars) == 0 # if all opened characters have been closed the list will be empty

##### Testing #####
print("Test #1: ([])[]({}) - True") # display test label
print(balanced('([])[]({})')) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: ([)] - False") # display test label
print(balanced('([)]')) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: ((() - False") # display test label
print(balanced('((()')) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #4: ((())) - True") # display test label
print(balanced('((()))')) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #5: [()]] - False") # display test label
print(balanced('[()]]')) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #6: {}{}{}{} - True") # display test label
print(balanced('{}{}{}{}')) # display test result
