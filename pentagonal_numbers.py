# Name: Alexis Raymond
# Date: Feb 24, 2020
# Exercise: Return the number of dots that exist in the whole pentagon on the Nth iteration. (https://edabit.com/challenge/st8mDxreMcuWxuz8c)

##### Method #####
def pentagonal(n): # calculates the number of dots in a pentagon of iteration N
	if(n == 1): # if calculating the first iteration, return 1
		return 1

	return (n-1)*5 + pentagonal(n-1) # use recursion to add the number of dots in the outside ring of all iterations up to N

##### Testing #####
print("Test 1: 1") # display test label
print(pentagonal(1)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 3: 16") # display test label
print(pentagonal(3)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 8: 141") # display test label
print(pentagonal(8)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 10: 226") # display test label
print(pentagonal(10)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 15: 526") # display test label
print(pentagonal(15)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 33: 2641") # display test label
print(pentagonal(33)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 43: 4516") # display test label
print(pentagonal(43)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 13: 391") # display test label
print(pentagonal(13)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 50: 6126") # display test label
print(pentagonal(50)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 62: 9456") # display test label
print(pentagonal(62)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test 21: 1051") # display test label
print(pentagonal(21)) # display result of method