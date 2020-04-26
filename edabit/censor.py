# Name: Alexis Raymond
# Date: April 6, 2020
# Exercise: Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char (https://edabit.com/challenge/zJSF5EfPe69e9sJAc)

##### Method #####
def censor(txt, lst, char): # return the censored string
	txtLst = txt.split() # convert the string to a list of words

	for i in range(len(txtLst)): # iterate through the words in the string
		if(txtLst[i] in lst): # if the word is in the list of censored words
			txtLst[i] = char * len(txtLst[i]) # replace the word with the defined char repeated the length of the word

	return " ".join(txtLst) # return the list converted to a string
	

##### Testing #####
print("Test #1: Today is a Wednesday!, [Today, a], -") # display test label
print(censor("Today is a Wednesday!", ["Today", "a"], "-")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: The cow jumped over the moon., [cow, over], *") # display test label
print(censor("The cow jumped over the moon.", ["cow", "over"], "*")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: Why did the chicken cross the road?, [Did, chicken, road], *") # display test label
print(censor("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*")) # display test result
