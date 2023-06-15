# Brute force 
# Time complexity: O(n^n) , n to the power of n, not n squared(n^2)
# Space complexity: O(1)

# class Solution:
#    mingiven = 1<<31
#    def coinChange(self, coins, amount):
#       def getMinCoins(amt, num_given):
#          if amt == 0:
#              self.mingiven = min(self.mingiven, num_given)
#          elif amt < 0: return
#          for coin in coins:
#             getMinCoins(amt-coin, num_given+1)
#       for coin in coins:
#          getMinCoins(amount-coin, 1)
#       return self.mingiven if self.mingiven != 1<<31 else -1
# a = Solution()
# print(a.coinChange([1, 3, 4, 5], 7))


# Dynamic programmint approach
# Time complexity: O(m*n) where m is the amount and n is the length of the coins array
# space complexity: O(n), where n is the amount
def coinChange(coins, amount):
   dp = [0] + [amount+1] * (amount)
   for i in range(1, amount+1):
      for coin in coins:
         if i-coin >= 0:
            dp[i] = min(dp[i], 1+dp[i-coin])
   return dp[amount] if dp[amount] != amount+1 else -1
    

print(coinChange([1, 3, 4, 5], 7))
