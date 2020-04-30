# Name: Alexis Raymond
# Date: April 30, 2020
# Exercise: Create a function that takes the width, height and character and returns a picture frame as a 2D list. (https://edabit.com/challenge/wEr6R9kc5oG88FRYy)

##### Method #####
def getFrame(w, h, char): # returns a frame with the dimensions specified
	if (w <= 2 or h <= 2): # if the width or the height are of 2 or less
		return "invalid" # return invalid because nothing can be placed inside

	frame = [] # create an empty list to contain the frame

	for i in range(h): # iterate through the rows in the frame
		if (i == 0 or i == h - 1): # if its the first or last row
			frame.append([char * w]) # add a full line of characters to the frame

		else: # if its not the first or last row
			frame.append([char + " " * (w - 2) + char]) # add a line with only characters at the beggining and at the end

	return frame # return the frame

##### Testing #####
print("Test #1: 4 - 5 - #") # display test label
for row in getFrame(4, 5, "#"): # iterate through the rows in the frame
	print(row) # print the row
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: 10 - 3 - *") # display test label
for row in getFrame(10, 3, "*"): # iterate through the rows in the frame
	print(row) # print the row
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 2 - 5 - 0") # display test label
print(getFrame(2, 5, "0"))
