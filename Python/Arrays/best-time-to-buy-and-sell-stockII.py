# Medium

def maxProfit(self, prices: List[int]) -> int:
    maxprofit = 0
    last_stock = prices[0]
    for price in prices:
        if price > last_stock:
            maxprofit += price-last_stock
        last_stock = price
    return maxprofit

