# Name: Alexis Raymond
# Date: April 17, 2020
# Exercise: A robot has been given a list of movement instructions. Each instruction is either left, right, up or down, followed by a distance to move. The robot starts at [0, 0]. You want to calculate where the robot will end up and return its final position as a list. (https://edabit.com/challenge/bupEio82q8NMnovZx)

##### Method #####
def trackRobot(movements): # returns the position of an object after several movements
	position = [0,0] # the object starts at position (0,0)

	for movement in movements: # iterate through the movements passed in instructions
		direction = movement.split()[0] # retrieve the direction of the movement
		length = int(movement.split()[1]) # retrieve the length of the movement

		if (direction == "left"): # if the movement is towards the left
			position[0] -= length # substract the length of the movement from the x coordinate

		elif (direction == "right"): # if the movement is towards the right
			position[0] += length # add the length of the movement to the x coordinate

		elif (direction == "up"): # if the movement is upwards
			position[1] += length # add the length of the movement to the y coordinate

		else: # if the movement is downwards
			position[1] -= length # substract the length of the movement from the y coordinate

	return position # return the position of the object after all the movements have been recorded

##### Testing #####
print("Test #1: [right 10, up 50, left 30, down 10]") # display test label
print(trackRobot(["right 10", "up 50", "left 30", "down 10"])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: []") # display test label
print(trackRobot([])) # display test result
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: [right 100, right 100, up 500, up 10000]") # display test label
print(trackRobot(["right 100", "right 100", "up 500", "up 10000"])) # display test result