# Name: Alexis Raymond
# Date: May 17, 2020
# Exercise: Create a function that takes an integer n and returns the identity matrix of n x n dimensions. (https://edabit.com/challenge/QN4RMpAnktNvMCWwg)

##### Method #####
def idMtrx(n): # returns the identity matrix of a given n
	try: # try to generate the identity matrix with the given n
		matrix = [] # create an empty list to contain the identity matrix

		if (n > 0): # if n is positive
			for row in range(n): # iterate through the rows in the matrix
				matrix.append([(1 if col == row else 0) for col in range(n)]) # add 1 to the right place in the row and 0 everywhere else

		elif (n < 0): # if n is negative
			for row in range(n * -1): # iterate through the rows in the matrix
				matrix.append([(1 if (n * -1) - col - 1 == row else 0) for col in range(n * -1)]) # add 1 to the right place in the row and 0 everywhere else

		return matrix # return the identity matrix

	except: # if n is not valid
		return "Error" # return "Error"

##### Testing #####
print("Test #1: 2") # display test label
for row in idMtrx(2): # iterate through the rows in the matrix
	print(row) # print the row
print("------------------------\n") # show a line to separate the tests

print("Test #2: -2") # display test label
for row in idMtrx(-2): # iterate through the rows in the frame
	print(row) # print the row
print("------------------------\n") # show a line to separate the tests

print("Test #3: 6") # display test label
for row in idMtrx(6): # iterate through the rows in the frame
	print(row) # print the row
print("------------------------\n") # show a line to separate the tests

print("Test #4: 0") # display test label
print(idMtrx(0))