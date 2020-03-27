# Name: Alexis Raymond
# Date: Mar 27, 2020
# Exercise: Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word.

##### Method #####
def is_palindrome(word): # returns whether the word is a palindrome or not
	return list(word) == list(word)[::-1] # checks if the word is the same in reverse

def shortest_palindrome(word): # returns the palindrome that can be created by adding the fewest number of letters to the word
	if(is_palindrome(word)): # if the word is already a palindrome, return the word
		return word

	alphabet = 'abcdefghijklmnopqrstuvwxyz' # create a list of all the letters in the alphabet

	possibilities = [] # create an empty list to contain all the possibilities

	for i in range(len(word) + 1): # iterate through the number of letters in the word
		for letter in alphabet: # iterate through the letters in the alphabet
			copy = list(word) # create a copy of the word in the form of a list
			copy.insert(i, letter) # insert the iterated letter in the iterated spot of the word
			
			if(is_palindrome(''.join(copy))): # if the new word is a palindrome, return it
				return ''.join(copy)

			possibilities.append(''.join(copy)) # if it is not a palindrome, add it to the list of possibilities

	while 1 == 1: # create an infinite loop
		for possibility in possibilities: # iterate through all the possibilities already found
			for i in range(len(possibility) + 1): # iterate through the number of letters in the possibility
				for letter in alphabet: # iterate through the letters in the alphabet
					copy = list(possibility) # create a copy of the possibility in the form of a list
					copy.insert(i, letter) # insert the iterated letter in the iterated spot of the possibility

					if(is_palindrome(''.join(copy))): # if the new word is a palindrome, return it
						return ''.join(copy)

					possibilities.append(''.join(copy)) # if it is not a palindrome, add it to the list of possibilities


##### Testing #####
print("Test #1: google") # display test label
print(shortest_palindrome("google")) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: race") # display test label
print(shortest_palindrome("race")) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: ab") # display test label
print(shortest_palindrome("ab")) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #4: abc") # display test label
print(shortest_palindrome("abc")) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #5: home") # display test label
print(shortest_palindrome("home")) # display test result