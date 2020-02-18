# Name: Alexis Raymond
# Date: Feb 18, 2020
# Exercise: use the recursive and loop methods to generate and display the n first terms of the fibonacci sequence


##### Recursive method #####
def recFib(n) : # returns the nth number of the fibonacci sequence using the recursive method
	if(n <= 1) : # if n is smaller or equal to 1, return n because the two first terms of the fibonacci sequence are 0 and 1 respectively
		return n

	return recFib(n-1) + recFib(n-2) # if n is greater than 1, return the sum of the 2 previous numbers of the fibonacci sequence

def printFib(n) : # displays the n first terms of the fibonacci sequence using the recFib method
	for i in range(n) : # loop through the numbers 0 to n (non-inclusively)
		print(recFib(i), end=" ") # display the ith number of the fibonacci sequence separated by spaces

	print("") # once all the numbers have been shown, skip a line

##### Loop method #####
def loopFib(n) : # displays the n first terms of the fibonacci sequence using the loop method
	sequence = [] # create an empty list to hold the numbers in the sequence

	for i in range(n) : # loop through the numbers 0 to n (non-inclusively)
		if(i <= 1) : # if n is smaller or equal to 1, add n to the sequence because the two first terms of the fibonacci sequence are 0 and 1 respectively
			sequence.append(i)
		
		else: # if n is greater than 1, add the sum of the two previous numbers to the sequence
			sequence.append(sequence[i-1] + sequence[i-2])

	for term in sequence : # loop through all the terms in the sequence
		print(term, end=" ") # display the terms in the sequence separated by spaces

	print("") # once all the numbers have been shown, skip a line

##### Testing the two methods for the first 10 terms of the fibonacci sequence #####
for i in range(1,11) : # loop through the numbers 1 to 10
	print("Term #", i, sep="") # display the number of terms to show
	
	print("Loop method: ", end="") # display a label for the loop method
	loopFib(i) # generate and display the "i" first numbers of the fibonacci sequence using the loop method
	
	print("Recursive method: ", end="") # display a label for the recursive method
	printFib(i) # generate and display the "i" first numbers of the fibonacci sequence using the recursive method
	
	print("------------------------------") # show a line to separate the sequences