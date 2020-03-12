# Name: Alexis Raymond
# Date: Mar 12, 2020
# Exercise: Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

##### Method #####
def numberOfRooms(classes): # returns the minimum number of rooms needed for a schedule
	if(len(classes) == 1): # return 1 if there is only 1 class scheduled
		return 1

	times = set() # create an empty set for all the time indices (sets are ideal because they don't accept duplicates)

	for lecture in classes: # iterate through all the lectures in the schedule
		times.add(lecture[0]) # add the start time to the set of indices
		times.add(lecture[1]) # add the end time to the set of indices

	times = sorted(list(times)) # convert the set of indices to a sorted list

	overlaps = [] # create an empty list to hold the number of classes overlapping at each time index

	for time in times: # iterate through all the time indices
		overlapCount = 0 # create a variable to hold the count of overlaps at each time index

		for lecture in classes: # iterate through all the lectures in the schedule
			if((time >= lecture[0]) and (time < lecture[1])): # if the class is happening at this time index, add 1 to the count
				overlapCount += 1

		overlaps.append(overlapCount) # add the overlap count to the list with all the time indices

	return max(overlaps) # return the max number of overlaps during the schedule (minimum number of rooms needed)

##### Testing #####
print("Test #1 (answer = 1)") # display test label
print(numberOfRooms([(0,25)])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2 (answer = 1)") # display test label
print(numberOfRooms([(0,25), (25,50), (50,75)])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3 (answer = 3)") # display test label
print(numberOfRooms([(0,25), (0,50), (24,75), (50,100), (100,125), (100, 150)])) # display test result
print("---------------\n") # show a line to separate the tests




