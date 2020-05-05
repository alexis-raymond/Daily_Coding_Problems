# Name: Alexis Raymond
# Date: May 5, 2020
# Exercise: Given a list of math equations (given as strings), return the percentage of correct answers as a string. Round to the nearest whole number. (https://edabit.com/challenge/3r7z6pkGnd4u7eZAd)

##### Method #####
def mark_maths(lst): # returns the percentage of right answers
	count = 0 # create a variable to hold the count of right answers

	for equation in lst: # iterate through the equations
		if (("+" in equation) and (int(equation[:equation.find("+")]) + int(equation[equation.find("+") + 1:equation.find("=")]) == int(equation[equation.find("=") + 1:]))): # if its an addition and the answer is right
			count += 1 # add 1 to the count

		if (("-" in equation[:equation.find("=")]) and (int(equation[:equation.find("-")]) - int(equation[equation.find("-") + 1:equation.find("=")]) == int(equation[equation.find("=") + 1:]))): # if its a substraction and the answer is right
			count += 1 # add 1 to the count

	return str(int(round((count / len(lst)) * 100))) + "%" # convert the count to a percentage and return this value

##### Testing #####
print("Test #1: ['2+2=4', '3+2=5', '10-3=3', '5+5=10']") # display test label
print(mark_maths(['2+2=4', '3+2=5', '10-3=3', '5+5=10'])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: ['1-2=-2']") # display test label
print(mark_maths(['1-2=-2'])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: ['2+3=5', '4+4=9', '3-1=2']") # display test label
print(mark_maths(['2+3=5', '4+4=9', '3-1=2'])) # display test result