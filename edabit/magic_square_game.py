# Name: Alexis Raymond
# Date: May 10, 2020
# Exercise: Write a function that returns True if the magic square game is won and False otherwise. (https://edabit.com/challenge/shf4iTJTbQ7sethFA)

##### Method #####
def magicSquareGame(alice, bob): # checks if Alice and Bob win the magic square game
	return bob[1][alice[0] - 1] == alice[1][bob[0] - 1] # returns whether the intersecting number is the same

##### Testing #####
print('Test #1: [2, "100"], [1, "101"]') # display test label
print(magicSquareGame([2, "100"], [1, "101"])) # display test result
print("-----------------\n") # show a line to separate the tests

print('Test #2: [2, "001"], [1, "101"]') # display test label
print(magicSquareGame([2, "001"], [1, "101"])) # display test result
print("-----------------\n") # show a line to separate the tests

print('Test #3: [3, "111"], [2, "011"]') # display test label
print(magicSquareGame([3, "111"], [2, "011"])) # display test result
print("-----------------\n") # show a line to separate the tests

print('Test #4: [1, "010"], [3, "101"]') # display test label
print(magicSquareGame([1, "010"], [3, "101"])) # display test result