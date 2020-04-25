# Name: Alexis Raymond
# Date: April 25, 2020
# Exercise: Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels. (https://edabit.com/challenge/jwiJNMiCW6P5d2XXA)

##### Method #####
def doesRhyme(txt1, txt2): # returns whether the last word in two strings contains the same vowels
	txt1 =  txt1.split()[-1].strip('.?!').lower() # keep only the lowercase version of the last word of string 1 without punctuation
	txt2 =  txt2.split()[-1].strip('.?!').lower() # keep only the lowercase version of the last word of string 2 without punctuation

	vowels_txt1 = [] # create an empty list to contain the vowels of string 1
	vowels_txt2 = [] # create an empty list to contain the vowels of string 2

	for char in txt1: # iterate through the characters in string 1
		if (char in 'aeiouy'): # if the character is a vowel
			vowels_txt1.append(char) # add the character to the list of vowels

	for char in txt2: # iterate through the characters in string 2
		if (char in 'aeiouy'): # if the character is a vowel
			vowels_txt2.append(char) # add the character to the list of vowels

	return sorted(vowels_txt1) == sorted(vowels_txt2) # return whether the 2 lists of vowels are the same when sorted

##### Testing #####
print("Test #1: Sam I am! - Green eggs and ham.") # display test label
print(doesRhyme("Sam I am!", "Green eggs and ham.")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: Sam I am! - Green eggs and HAM.") # display test label
print(doesRhyme("Sam I am!", "Green eggs and HAM.")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: You are off to the races - a splendid day.") # display test label
print(doesRhyme("You are off to the races", "a splendid day.")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: and frequently do? - you gotta move.") # display test label
print(doesRhyme("and frequently do?", "you gotta move.")) # display test result