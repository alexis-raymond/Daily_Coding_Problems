# Name: Alexis Raymond
# Date: Mar 26, 2020
# Exercise: Given a list of numbers, compute the running median.

##### Method #####
def median(numbers): # returns the median of a list of numbers
	numbers.sort() # sort the list of numbers

	if(len(numbers) % 2 == 0): # if it is an even-numbered list
		return (numbers[len(numbers) // 2] + numbers[(len(numbers) // 2) - 1]) / 2 # return the average of the two middle numbers

	return numbers[len(numbers) // 2]	# if it is an odd-numbered list, return the middle number


def running_median(numbers): # prints the running median of a list of numbers
	for i in range(len(numbers)): # iterate through the numbers 0 to the length of the list
		print(median(numbers[:i+1])) # print the median of the list of numbers up to the iterative


##### Testing #####
print("Test #1: [2, 1, 5, 7, 2, 0, 5]") # display test label
running_median([2,1,5,7,2,0,5]) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: [3,2]") # display test label
running_median([3,2]) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: [1,2,3,4,5,6]") # display test label
running_median([1,2,3,4,5,6]) # display test result