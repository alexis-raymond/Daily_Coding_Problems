# Name: Alexis Raymond
# Date: May 27, 2020
# Exercise: Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot. (https://edabit.com/challenge/A8gEGRXqMwRWQJvBf)

##### Method #####
def ticTacToe(board): 
	for row in board: # iterate through the rows on the board
		if (row[0] == row[1] == row[2] and row[0] != "E"): # if one row is all identical
			return row[0] # return the character in that row

	for col in range(3): # iterate through the columns in the board
		if (board[0][col] == board[1][col] == board[2][col] and board[0][col] != "E"): # if one col is all identical
			return board[0][col] # return the character in that col

	if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != "E"): # if the first diagonal is all identical
		return board[0][0] # return the character in the first diagonal

	if (board[0][2] == board[1][1] == board[2][0] and board[0][2] != "E"): # if the second diagonal is all identical
		return board[0][2] # return the character in the second diagonal

	return "Draw" # if no row, col or diagonal is identical, it's a draw

##### Testing #####
print("Test #1") # display test label
for row in [["X", "O", "X"], ["O", "X",  "O"], ["O", "X",  "X"]]: # iterate through the rows in the board
	print(row) # print the row
print(ticTacToe([["X", "O", "X"], ["O", "X",  "O"], ["O", "X",  "X"]])) # print the winner
print("------------------------\n") # show a line to separate the tests

print("Test #2") # display test label
for row in [["O", "O", "O"], ["O", "X", "X"], ["E", "X", "X"]]: # iterate through the rows in the board
	print(row) # print the row
print(ticTacToe([["O", "O", "O"], ["O", "X", "X"], ["E", "X", "X"]])) # print the winner
print("------------------------\n") # show a line to separate the tests

print("Test #3") # display test label
for row in [["X", "X", "O"], ["O", "O", "X"], ["X", "X", "O"]]: # iterate through the rows in the board
	print(row) # print the row
print(ticTacToe([["X", "X", "O"], ["O", "O", "X"], ["X", "X", "O"]])) # print the winner