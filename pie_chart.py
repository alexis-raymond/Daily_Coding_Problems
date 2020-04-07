# Name: Alexis Raymond
# Date: April 7, 2020
# Exercise: returns a map to design a pie chart, like to say the same dictionary with values transformed in degrees instead of frequencies. (https://edabit.com/challenge/GwCAximybWF6ANdLY)

##### Method #####
def pieChart(data): # returns a map to design a pie chart
	total_frequencies = 0 # initiate variable to hold the total frequencies for all elements

	for label in data: # for each element in the dictionary
		total_frequencies += data[label] # add the frequency for the current element to the running total

	for label in data: # for each element in the dictionary
		data[label] = round((data[label] / total_frequencies) * 360, 1) # change the frequency for the degrees required to build the pie chart

	return data # return the modified dictionary

##### Testing #####
print("Test #1: a: 1, b: 2") # display test label
print(pieChart({ "a": 1, "b": 2 })) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: a: 30, b: 15, c: 55") # display test label
print(pieChart({ "a": 30, "b": 15, "c": 55 })) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: a: 8, b: 21, c: 12, d: 5, e: 4") # display test label
print(pieChart({ "a": 8, "b": 21, "c": 12, "d": 5, "e": 4 })) # display test result