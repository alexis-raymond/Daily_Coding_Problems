# Name: Alexis Raymond
# Date: Mar 15, 2020
# Exercise: Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

##### Method #####
def balanced(expression):
	opposites = {
		"[": "]",
		"(": ")",
		"{": "}"
	}

	open_chars = []

	for char in expression:
		if(len(open_chars) == 0):
			open_chars.append(char)

		elif((open_chars[-1] in opposites) and (char == opposites[open_chars[-1]])):
			open_chars.pop()

		else:
			open_chars.append(char)

	return len(open_chars) == 0

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