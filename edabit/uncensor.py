# Name: Alexis Raymond
# Date: April 15, 2020
# Exercise: Given a censored string (vowels replaced with *) and a string of the censored vowels, return the original uncensored string. (https://edabit.com/challenge/ehyZvt6AJF4rKFfXT)

##### Method #####
def uncensor(txt, vowels): # return the uncensored version of the string
	num_censored = 0 # intialize a variable to hold which vowel we need to replace
	txt = list(txt) # convert the text to a list

	for i in range(len(txt)): # iterate through the numbers from 0 to the number of characters in the text
		if(txt[i] == "*"): # if the current character is censored
			txt[i] = vowels[num_censored] # replace the character with the vowel
			num_censored += 1 # add 1 to the current vowel

	return "".join(txt) # return the string version of the censored text

##### Testing #####
print("Test #1: Wh*r* d*d my v*w*ls g*? - eeioeo") # display test label
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: abcd - None") # display test label
print(uncensor("abcd", "")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: *PP*RC*S* - UEAE") # display test label
print(uncensor("*PP*RC*S*", "UEAE")) # display test result
