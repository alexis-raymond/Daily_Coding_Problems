# Name: Alexis Raymond
# Date: May 3, 2020
# Exercise: Write a function that adds two numbers. The catch, however, is that the numbers will be strings. (https://edabit.com/challenge/bwCDG9X8cJiAdvfxE)

##### Method #####
def addStrNums(num1, num2): # returns the result of 2 strings added to eachother
	try: # try to convert the text to numbers
		if(num1 == ""): # if the first number is empty
			num1 = "0" # change it to 0

		if(num2 == ""): # if the second number is empty
			num2 = "0" # change it to 0

		num1 = int(num1) # convert the first number to an integer
		num2 = int(num2) # convert the second number to an integer

	except: # if one of the texts is not a number
		return "-1" # return -1

	return str(num1 + num2) # return a string version of the two numbers added together

##### Testing #####
print("Test #1: 4, 5") # display test label
print(addStrNums("4", "5")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: abcdefg, 3") # display test label
print(addStrNums("abcdefg", "3")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 1, _") # display test label
print(addStrNums("1", "")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: 1874682736267235927359283579235789257, 32652983572985729") # display test label
print(addStrNums("1874682736267235927359283579235789257", "32652983572985729")) # display test result