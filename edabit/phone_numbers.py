# Name: Alexis Raymond
# Date: Feb 23, 2020
# Exercise: checks if the phone number is in a valid format (https://edabit.com/challenge/amYH2SMto4yZw9E6n)

##### Method #####
def validatePhone(phone_number): # checks if a phone number is in a valid format
	phone_number_list = list(phone_number) # convert the phone number to a list to iterate through the characters

	digits = '0123456789' # list the possible digits
	separators = '+-()./ ' # list the possible separators

	brackets = False # initiate a variable that holds if there are brackets in the phone number

	num_digits = 0 # initiate a variable to hold the number of digits
	for digit in digits: # iterate through all the possible digits
		num_digits += phone_number_list.count(digit) # add the count for that digit to the total count

	if((num_digits != 10) and (num_digits != 11)): # return false if the phone number does not have 10 or 11 digits
		return False

	for char in phone_number_list: # iterate through all the characters in the phone number
		if(char not in digits + separators): # return false if the character is not valid
			return False

	if((phone_number_list[0] == "+") and (phone_number_list[1] =="1")): # if regional code +1
		if(phone_number_list[2] not in digits): # if there is a separator after the regional code
			phone_number_list = phone_number_list[3:] # remove the regional code and the first separator

		else: # if there's no separator after the regional code
			phone_number_list = phone_number_list[2:] # remove the regional code

	elif((phone_number_list[0] == "1") and (num_digits == 11)): # if regional code 1
		if(phone_number_list[1] not in digits): # if there is a separator after the regional code
			phone_number_list = phone_number_list[2:] # remove the regional code and the first separator
		
		else: # if there's no separator after the regional code
			phone_number_list = phone_number_list[1:] # remove the regional code

	elif(num_digits != 10): # return false if there isn't a regional code but there are too many digits
		return False

	if((phone_number_list[0] == "(")): # if the first character is an opening bracket
		if(phone_number_list[4] != ")"): # return false if there isn't a closing bracket
			return False

		phone_number_list.pop(4) # remove the closing bracket from the phone number
		phone_number_list.pop(0) # remove the opening bracket from the phone number

		brackets = True # set the flag to true

	if(len(phone_number_list) == 10): # return true if there aren't any separators (all digits)
		return True

	elif(len(phone_number_list) == 12): # if there are 2 separators
		if(brackets and (phone_number_list[3] == " ") and (phone_number_list[7] == "-")): # return true if there are brackets, ensure the correct use of separators
			return True

		elif((phone_number_list[3] == phone_number_list[7]) and (phone_number_list[3] not in digits)): # return true if the separators are the same and are in the right positions
			return True

		else: # return false if the separators are not used properly
			return False

	else: # return false if the number of characters is incorrect
		return False

##### Testing #####
print("Test #1: +1-892-445-7663 / True") # display test label
print(validatePhone("+1-892-445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2: 1-892-445-7663 / True") # display test label
print(validatePhone("1-892-445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3: 1 (892) 445-7663 / True") # display test label
print(validatePhone("1 (892) 445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4: 1.892.567.8901 / True") # display test label
print(validatePhone("1.892.567.8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #5: 1/892/567/8901 / True") # display test label
print(validatePhone("1/892/567/8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #6: 1 892 567 8901 / True") # display test label
print(validatePhone("1 892 567 8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #7: 18925678901 / True") # display test label
print(validatePhone("18925678901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #8: 892-445-7663 / True") # display test label
print(validatePhone("892-445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #9: (892) 445-7663 / True") # display test label
print(validatePhone("(892) 445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #10: 892.567.8901 / True") # display test label
print(validatePhone("892.567.8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #11: 892/567/8901 / True") # display test label
print(validatePhone("892/567/8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #12: 892 567 8901 / True") # display test label
print(validatePhone("892 567 8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #13: 8925678901 / True") # display test label
print(validatePhone("8925678901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #14: 89-445-7663 / False") # display test label
print(validatePhone("89-445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #15: (892) 4454-7663 / False") # display test label
print(validatePhone("(892) 4454-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #16: 892  567 8901 / False") # display test label
print(validatePhone("892  567 8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #17: 892?567?8901 / False") # display test label
print(validatePhone("892?567?8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #18: !1-892-567-8901 / False") # display test label
print(validatePhone("!1-892-567-8901")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #19: (8924) 445-7663 / False") # display test label
print(validatePhone("(8924) 445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #20: 12 892 445-7663 / False") # display test label
print(validatePhone("12 892 445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #21: 1&892&445-7663 / False") # display test label
print(validatePhone("1&892&445-7663")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #22: 894-445-766 / False") # display test label
print(validatePhone("894-445-766")) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests