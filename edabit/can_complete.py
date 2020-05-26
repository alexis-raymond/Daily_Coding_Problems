# Name: Alexis Raymond
# Date: May 26, 2020
# Exercise: Create a function that, given an input string, determines if the word can be completed. (https://edabit.com/challenge/bd2fLqAxHfGTx86Qx)

##### Method #####
def canComplete(initial, word): # checks if the word can be completed from the input string
	if (not all([initial.count(char) <= word.count(char) for char in initial])): # if all characters in the initial don't appear the same number of times in the word
		return False # return false

	return all([word.index(initial[i]) < word.index(initial[i + 1]) for i in range(len(initial) - 1)]) # return true if all letters in the initial appear in the same order in the owrd and false otherwise

##### Testing #####
print('Test #1: "butl", "beautiful"') # display test label
print(canComplete("butl", "beautiful")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print('Test #2: "butlz", "beautiful"') # display test label
print(canComplete("butlz", "beautiful")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print('Test #3: "tulb", "beautiful"') # display test label
print(canComplete("tulb", "beautiful")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print('Test #4: "bbutl", "beautiful"') # display test label
print(canComplete("bbutl", "beautiful")) # display test result