# Name: Alexis Raymond
# Date: Feb 20, 2020
# Exercise: given a positive number n, check if n or the binary representation of n is palindromic (https://edabit.com/challenge/QuxCNBLcGJReCawjz)

##### Method #####
def palindromeType(n): # returns strings that describe whether the number is a palindrome or not
	decimal = list(str(n)) == list(str(n))[::-1] # assess whether the number is the same read forward and backward
	binary = list(str(bin(n)))[2:] == list(str(bin(n)))[2:][::-1] # assess whether the binary form of the number is the same read forward and backward

	if((decimal) and (binary)): # if both decimal and binary forms of the number are palindromes
		return "Decimal and binary."

	if(decimal): # if only the decimal form of the number is a palindrome
		return "Decimal only."

	if(binary): # if only the binary form of the number is a palindrome
		return "Binary only."

	return "Neither!" # if neither forms of the number are palindromes

##### Testing #####
print("Test #1") # display test label
print("Decimal form: 1306031") # display decimal form of number
print("Binary form:", bin(1306031)) # display binary form of number
print(palindromeType(1306031)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #2") # display test label
print("Decimal form: 427787") # display decimal form of number
print("Binary form:", bin(427787)) # display binary form of number
print(palindromeType(427787)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #3") # display test label
print("Decimal form: 313") # display decimal form of number
print("Binary form:", bin(313)) # display binary form of number
print(palindromeType(313)) # display result of method
print("--------------------------------------------\n") # show a line to separate the tests

print("Test #4") # display test label
print("Decimal form: 934") # display decimal form of number
print("Binary form:", bin(934)) # display binary form of number
print(palindromeType(934)) # display result of method
