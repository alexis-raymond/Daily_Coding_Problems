# Name: Alexis Raymond
# Date: April 11, 2020
# Exercise: Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper. (https://edabit.com/challenge/76ibd8jZxvhAwDskb)

##### Method #####
def tallestSkyscraper(lst): # returns the height of the highest building in the skyline
	buildings = [0] * len(lst[0]) # create a list to capture the height of each building

	for level in lst: # iterate over the levels in the skyline
		for i in range(len(lst[0])): # iterate over the number of buildings there are
			buildings[i] += level[i] # add 1 if the building reaches that level

	return max(buildings) # return the tallest building

##### Testing #####
print("Test #1: [0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]") # display test label
print(tallestSkyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]") # display test label
print(tallestSkyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]") # display test label
print(tallestSkyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
])) # display test result