# Name: Alexis Raymond
# Date: Feb 18, 2020
# Exercise: given a list of numbers and a number k, return whether any two numbers from the list add up to k (daily coding problem 1)


##### Method ##### 
def sumToK(list_of_num, k): # returns true if two numbers in the list add up to k and false otherwise
	for num1 in range(len(list_of_num)): # iterate through all the indexes of the list of numbers
		for num2 in range(len(list_of_num)): # iterate through all the indexes of the list of numbers again
			if((num1 != num2) and (list_of_num[num1] + list_of_num[num2] == k)): # if both numbers are not the same but add up to k return True
				return True

	return False # if none of the combinations returned True, return False

##### Testing 4 use cases #####
print(sumToK([10,15,3,7], 17)) # True
print(sumToK([10,2,3], 15)) # False
print(sumToK([8,2,3,7], 5)) # True
print(sumToK([1,1,1,2], 2)) # True