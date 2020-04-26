# Name: Alexis Raymond
# Date: Feb 22, 2020
# Exercise: given a number n, checks whether the number is uban (does not contain the letter u when spelled out). From https://edabit.com/challenge/rRKbaDKxzBhaLAFJZ

##### Method #####
def isUban(n): # checks whether the number is uban (does not contain the letter u when spelled out); works from 1 to 9 999 999
	if(list(str(n))[-1] == "4"): # if the first digit is 4 -> not uban
		return False

	if((n >= 100) and (n < 1000000)): # if the number is between 100 and 999 999 (inclus.) -> not uban
		return False

	if((n >= 1000000) and (list(str(n))[0]) == "4"): # if the number is greater or equal to 1 000 000, and the first digit is 4 -> not uban
		return False

	if((n >= 1000000) and (int(str(n)[1:]) >= 100)): # if the number is greater or equal to 1 000 000, and it contains the words hundred or thousand -> not uban
		return False

	return True # if all the tests were passed successfuly, the number is uban


##### Testing #####
print("Test #1: n = 24 (False)") # display test label
print(isUban(24)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: n = 223 (False)") # display test label
print(isUban(223)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: n = 2051 (False)") # display test label
print(isUban(2051)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: n = 627 (False)") # display test label
print(isUban(627)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #5: n = 6258 (False)") # display test label
print(isUban(6258)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #6: n = 12 (True)") # display test label
print(isUban(12)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #7: n = 202 (False)") # display test label
print(isUban(202)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #8: n = 98 (True)") # display test label
print(isUban(98)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #9: n = 6592 (False)") # display test label
print(isUban(6592)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #10: n = 393 (False)") # display test label
print(isUban(393)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #11: n = 1000096 (True)") # display test label
print(isUban(1000096)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #12: n = 40 (True)") # display test label
print(isUban(40)) # display result of method
