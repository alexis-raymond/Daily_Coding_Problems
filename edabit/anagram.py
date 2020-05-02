# Name: Alexis Raymond
# Date: May 2, 2020
# Exercise: Write a function that returns True if a given name can generate an array of words. (https://edabit.com/challenge/sDvjdcBrbHoXKvDsZ)

##### Method #####
def anagram(name, words): # checks if a list of words is an anagram for a name
	if (len(name.replace(" ", "")) != len("".join(words))): # if the name and the list of words don't have the same number of characters
		return False # return False

	for char in "".join(words).lower(): # iterate through the characters in all the words
		if (name.lower().count(char) != "".join(words).lower().count(char) and char != " "): # if the characer is not present the same number of times in both texts
			return False # return False

	return True # return True

##### Testing #####
print("Test #1: Justin Bieber - [injures, ebb, it]") # display test label
print(anagram("Justin Bieber", ["injures", "ebb", "it"])) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #2: Natalie Portman - [ornamental, pita]") # display test label
print(anagram("Natalie Portman", ["ornamental", "pita"])) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #3: Chris Pratt - [chirps, rat]") # display test label
print(anagram("Chris Pratt", ["chirps", "rat"])) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #4: Jeff Goldblum - [jog, meld, bluffs]") # display test label
print(anagram("Jeff Goldblum", ["jog", "meld", "bluffs"])) # display test result