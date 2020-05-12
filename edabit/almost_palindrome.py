# Name: Alexis Raymond
# Date: May 12, 2020
# Exercise: A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function that returns True if a string is an almost-palindrome and False otherwise. (https://edabit.com/challenge/APNhiaMCuRSwALN63)

##### Method #####
def almostPalindrome(txt): # checks if some text requires only one change to be a palindrome
	count = 0 # create a variable to hold the number of changes necessary

	for i in range(len(txt) // 2): # iterate through the numbers 0 to half the length of the text
		if (txt[i] != txt[len(txt) - i - 1]): # if the iterated character is not the same as its reverse
			count += 1 # add one change to the count

	return count == 1 # return True if one change is necessary and False otherwise

##### Testing #####
print("Test #1: abcdcbg") # display test label
print(almostPalindrome("abcdcbg")) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #2: abccia") # display test label
print(almostPalindrome("abccia")) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #3: abcdaaa") # display test label
print(almostPalindrome("abcdaaa")) # display test result
print("-----------------\n") # show a line to separate the tests

print("Test #4: 1234312") # display test label
print(almostPalindrome("1234312")) # display test result
print("-----------------\n") # show a line to separate the tests