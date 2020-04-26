# Name: Alexis Raymond
# Date: April 19, 2020
# Exercise: Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise. (https://edabit.com/challenge/WS6hR6b9EZzuDTD26)

##### Method #####
def noDuplicateLetters(phrase): # returns true if all the words contain unique letters and false otherwise
	for word in phrase.split(): # iterate through the words in the phrase
		for letter in word: # iterate through the letters in the word
			if(word.count(letter) > 1): # if that letter is present more than once in the word
				return False # return False
	
	return True # if there are no words with duplicate letters, return True

##### Testing #####
print("Test #1: Fortune favours the bold.") # display test label
print(noDuplicateLetters("Fortune favours the bold.")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: You can lead a horse to water, but you can't make him drink.") # display test label
print(noDuplicateLetters("You can lead a horse to water, but you can't make him drink.")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: Look before you leap.") # display test label
print(noDuplicateLetters("Look before you leap.")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: An apple a day keeps the doctor away.") # display test label
print(noDuplicateLetters("An apple a day keeps the doctor away.")) # display test result