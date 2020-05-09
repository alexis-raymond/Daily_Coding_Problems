# Name: Alexis Raymond
# Date: May 9, 2020
# Exercise: Write a function that returns True if it's possible to build a phrase txt1 using only the characters from another phrase txt2. (https://edabit.com/challenge/CD2fqbytBuXrbqJkL)

##### Method #####
def canBuild(txt1, txt2): # checks if you can build a string with the text from another string
	txt2 = list(txt2) # convert the second text to a list

	for char in txt1: # iterate through the characters in the first string
		if (char != " "): # if the character is not a whitespace
			try: # try to remove the iterated character from the second string
				txt2.remove(char)

			except: # if the iterated character is not in the second string, return False
				return False

	return True # if all the characters from the first string were succesfully removed from the second string, return True

##### Testing #####
print('Test #1: "got 2 go", "gogogo 2 today"') # display test label
print(canBuild("got 2 go", "gogogo 2 today")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print('Test #2: "sit on top", "its a moo point"') # display test label
print(canBuild("sit on top", "its a moo point")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print('Test #3: "long high add or", "highway road go long"') # display test label
print(canBuild("long high add or", "highway road go long")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print('Test #4: "fill tuck mid", "truck falls dim"') # display test label
print(canBuild("fill tuck mid", "truck falls dim")) # display test result