# Name: Alexis Raymond
# Date: April 10, 2020
# Exercise: Given the month and year as numbers, return whether that month contains a Friday 13th. (https://edabit.com/challenge/Xkc2iAjwCap2z9N5D)

##### Method #####
import datetime # import the datetime module for python

def hasFriday13(month, year): # returns whether the specified month contains a friday the 13th
	return datetime.date(year, month, 13).weekday() == 4 # return true if the 13th day of the specified month is a friday and false otherwise


##### Testing #####
print("Test #1: March 2020") # display test label
print(hasFriday13(3, 2020)) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: October 2017") # display test label
print(hasFriday13(10, 2017)) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: January 1985") # display test label
print(hasFriday13(1, 1985)) # display test result