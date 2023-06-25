# Easy

def maxProfit(prices):
	maxP = 0
	minBuy = prices[0]
	for price in prices:
		if price < minBuy:
			minBuy = price
		maxP = max(maxP, price-minBuy)
	return maxP

print(maxProfit(prices = [7,1,5,3,6,4]))