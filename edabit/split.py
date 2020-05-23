# Name: Alexis Raymond
# Date: May 23, 2020
# Exercise: Write a function that groups a string into parentheses cluster. Each cluster should be balanced. (https://edabit.com/challenge/Fpymv2HieqEd7ptAq)

##### Method #####
def split(txt): # returns all the paratheses cluster in some text
	i = 2 # start the iterator at the 3rd character in the text
	clusters = [] # create an empty list to hold all the clusters

	while (i <= len(txt)): # run the following code as long as the iterator is not the last character of the text
		if (txt[:i].count("(") == txt[:i].count(")")): # if the subset of the list up to the iterator is balanced
			clusters.append(txt[:i]) # add the subset to the list of clusters
			txt = txt[i:] # remove the subset from the text
			i = 2 # reinitiate the iterator

		else: # if the subset is not balanced
			i += 1 # add one to the iterator

	return clusters # return the list of clusters

##### Testing #####
print("Test #1: ()()()") # display test label
print(split("()()()")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: ((()))") # display test label
print(split("((()))")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: ((()))(())()()(()())") # display test label
print(split("((()))(())()()(()())")) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: ((())())(()(()()))") # display test label
print(split("((())())(()(()()))")) # display test result