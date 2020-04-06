# Name: Alexis Raymond
# Date: April 5, 2020
# Exercise: Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once.

##### Method #####
def maxProfit(stock_prices): # returns the most profit that can be made by buying and selling stocks
	max_profit = -1000000000000 # initiate the max profit with a extremely small number

	for i in range(len(stock_prices)): # iterate through all the stock prices
		for x in range(i+1, len(stock_prices)): # iterate through all the stock prices after the current day
			if(stock_prices[x] - stock_prices[i] > max_profit): # if the profit is larger than max profit
				max_profit = stock_prices[x] - stock_prices[i] # set the max profit to the new profit

	return max_profit # return the max profit

##### Testing #####
print("Test #1: [9, 11, 8, 5, 7, 10]") # display test label
print(maxProfit([9, 11, 8, 5, 7, 10])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #2: [9, 6]") # display test label
print(maxProfit([9, 6])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: [9, 10, 11, 12]") # display test label
print(maxProfit([9, 10, 11, 12])) # display test result
print("---------------\n") # show a line to separate the tests

print("Test #3: [9, 8, 8, 5, 7, 18]") # display test label
print(maxProfit([9, 8, 8, 5, 7, 18])) # display test result