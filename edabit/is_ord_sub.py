# Name: Alexis Raymond
# Date: May 8, 2020
# Exercise: Write a function that, given lists smlst and biglst, decides if smlst is an ordered sublist of biglst. (https://edabit.com/challenge/vLRpikwB9dqaR3HAj)

##### Method #####
def isOrdSub(smlst, biglst): # checks whether the small list is an ordered subset of the big list
	smlst = smlst[::-1] # reverse the order of the small list

	for num in biglst: # iterate through the numbers in the big list
		if(len(smlst) > 0 and num == smlst[-1]): # if the small list is not empty and the iterated number is the same as the last number of the small list
			smlst.pop() # remove the last number of the small list

	return len(smlst) == 0 # return True if the small list is empty and False otherwise

##### Testing #####
print("Test #1: [4,3,2] - [5,4,3,2,1]") # display test label
print(isOrdSub([4,3,2], [5,4,3,2,1])) # display test result
print("--------------\n") # show a line to separate the tests

print("Test #2: [5,3,1] - [5,4,3,2,1]") # display test label
print(isOrdSub([5,3,1], [5,4,3,2,1])) # display test result
print("--------------\n") # show a line to separate the tests

print("Test #3: [5,3,1] - [1,2,3,4,5]") # display test label
print(isOrdSub([5,3,1], [1,2,3,4,5])) # display test result
print("--------------\n") # show a line to separate the tests

print("Test #4: [1,2,3] - [3,2,1,2,3]") # display test label
print(isOrdSub([1,2,3], [3,2,1,2,3])) # display test result