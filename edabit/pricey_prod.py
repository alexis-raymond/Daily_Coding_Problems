# Name: Alexis Raymond
# Date: May 7, 2020
# Exercise: You will be given a dictionary with various products and their respective prices. Return a list of the products with a minimum price of 500 in descending order. (https://edabit.com/challenge/SxevRSmRcshgwnAKp)

##### Method #####
def priceyProd(d): # returns a list in descending order of the items priced 500$ or more
	keys = filter(lambda v: v >= 500, d.values()) # find the values greater or equal to 500

	keys.sort(reverse = True) # sort the values in descending order

	return list(map(lambda value: d.keys()[d.values().index(value)], keys))

	# return list(map(lambda value: d.keys()[d.values().index(value)], sorted(filter(lambda v: v >= 500, d.values()), reverse = True)))

##### Testing #####
print('Test #1: {"Computer" : 600, "TV" : 800, "Radio" : 50}') # display test label
print(priceyProd({"Computer" : 600, "TV" : 800, "Radio" : 50})) # display test result
print("-----------------\n") # show a line to separate the tests

print('Test #2: {"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}') # display test label
print(priceyProd({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501})) # display test result
print("-----------------\n") # show a line to separate the tests

print('Test #3: {"Loafers" : 50, "Vans" : 10, "Crocs" : 20}') # display test label
print(priceyProd({"Loafers" : 50, "Vans" : 10, "Crocs" : 20})) # display test result