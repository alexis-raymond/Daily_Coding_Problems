# Name: Alexis Raymond
# Date: April 12, 2020
# Exercise: Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged. (https://edabit.com/challenge/jwzAdBnJnBxCe4AXP)

##### Method #####
def rearrangedDifference(num): # return the difference between the highest and lowest numbers you can make by rearranging the digits
	highest_num = int("".join(sorted(str(num), reverse = True))) # highest number is when the digits are in descending order
	lowest_num = int("".join(sorted(str(num), reverse = False))) # lowest number is when the digits are in ascending order

	return highest_num - lowest_num # return the difference between the highest and lowest numbers possible

##### Testing #####
print("Test 1: 972882") # display test label
print(rearrangedDifference(972882)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 2: 3320707") # display test label
print(rearrangedDifference(3320707)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 3: 90010") # display test label
print(rearrangedDifference(90010)) # display result of method