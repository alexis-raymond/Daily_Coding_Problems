# Name: Alexis Raymond
# Date: May 18, 2020
# Exercise: Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it. (https://edabit.com/challenge/xbjDMxzpFcsAWKp97)

##### Method #####
def canSeeStage(seats): # returns whether everyone can see the stage
	for row in range(1, len(seats)): # iterate through the rows in the seating chart
		for col in range(len(seats[row])): # iterate through the columns in the seating chart
			if (seats[row][col] <= seats[row-1][col]): # if the number is smaller or equal to the number in front of him
				return False # return False

	return True # return True if there were no instances of people not seeing the stage

##### Testing #####
print("Test #1") # display test label
for row in [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]: # iterate through the rows in the seating chart
	print(row) # display the row
print(canSeeStage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])) # display test result
print("--------------------------------\n") # show a line to separate the tests

print("Test #2") # display test label
for row in [
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]: # iterate through the rows in the seating chart
	print(row) # display the row
print(canSeeStage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
])) # display test result
print("--------------------------------\n") # show a line to separate the tests

print("Test #3") # display test label
for row in [
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]: # iterate through the rows in the seating chart
	print(row) # display the row
print(canSeeStage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
])) # display test result
print("--------------------------------\n") # show a line to separate the tests

print("Test #4") # display test label
for row in [
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]: # iterate through the rows in the seating chart
	print(row) # display the row
print(canSeeStage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
])) # display test result