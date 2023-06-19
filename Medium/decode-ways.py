

def numDecodings(s:str) -> int:
	# brute force, O(2^len(s)) runtime and O(1) space
	'''
	def dfs(i):
		if i == len(s):
			return 1

		elif i>len(s) or s[i]=='0':
			return 0

		elif int(s[i:i+2]) > 26:
			return dfs(i+1)

		return  dfs(i+1) + dfs(i+2)

	return dfs(0)
	# '''

	# O(n) runtime, O(n) space
	# dp = [0] * (len(s)) + [1]
	# for i in range(len(s)-1, -1, -1):
	# 	if s[i]!='0':
	# 		dp[i] = dp[i+1]
	# 	if 10 <= int(s[i:i+2]) <= 27 :
	# 		dp[i] += dp[i+2]
	# print(dp)
	# return dp[0]

	# O(n) runtime, O(1) space
	curr_i, one, two = 0, 1, 0
	for i in range(len(s)-1, -1, -1):
		curr_i = 0 
		if s[i]!='0':
			curr_i = one
		if 10 <= int(s[i:i+2]) <= 27 :
			curr_i += two
		one, two = curr_i, one
		
	return curr_i



print(numDecodings('11106'))
print(numDecodings('121'))
print(numDecodings('131'))