
# Name: Alexis Raymond
# Date: April 16, 2020
# Exercise: Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list. (https://edabit.com/challenge/pQavNkBbdmvSMmx5x)

##### Method #####
def majorityVote(lst): # returns the element that forms the majority of the list
	if(len(lst) == 0): # if the list is empty
		return None # return None

	counts = {} # create a dictionary to hold the counts for each element in the list

	for element in lst: # iterate through the elements in the list
		if(element not in counts): # if the element is not yet in the dictionary
			counts[element] = lst.count(element) # add the count for that element to the dictionary

	for element in counts: # iterate through the element in the dictionary
		if(counts[element] > len(lst) / 2): # if the element appears more than half the length of the list
			return element # return the element

	return None # if no element forms a majority

##### Testing #####
print("Test #1: [A, A, B]") # display test label
print(majorityVote(["A", "A", "B"])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: [A, A, A, B, C, A]") # display test label
print(majorityVote(["A", "A", "A", "B", "C", "A"])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: [A, B, B, A, C, C]") # display test label
print(majorityVote(["A", "B", "B", "A", "C", "C"])) # display test result
