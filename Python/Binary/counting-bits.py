
def countBits(n:int) -> list[int]:
	dp = [0] * (n+1)
	exp = 2**0
	for i in range(1, n+1):
		if i == exp << 1:
			exp = i
		dp[i] = 1 + dp[i-exp]
	return dp 


print(countBits(9))