# Name: Alexis Raymond
# Date: Mar 29, 2020
# Exercise: Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary.

##### Method #####
def itinerary(flights, starter): # return someone's itinerary given his flights and starting airport
	itinerary = [starter] # create the list that will contain the itinerary

	while len(flights) > 0: # as long as not all flights have been used
		for flight in flights: # iterate through the remaining flights
			if(flight[0] == itinerary[len(itinerary) - 1]): # if the iterated flight starts at the last airport in the itinerary
				itinerary.append(flight[1]) # add the flight to the itinerary
				flights.remove(flight) # remove the flight from the list of flights

	return itinerary # return the itinerary


##### Testing #####
print("Test #1: [(SFO, HKO), (YYZ, SFO), (YUL, YYZ), (HKO, ORD)], YUL") # display test label
print(itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], A") # display test label
print(itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')) # display test result