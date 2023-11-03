# Medium

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    last_stock = prices[0]
    for price in prices:
        if price > last_stock:
            profit += price-last_stock
        last_stock = price
    return profit

