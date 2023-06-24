
def longestCommonSubsequence(text1: str, text2: str) -> int:
	# In this solution, we store a n*m matrix in the dp array
	'''
	dp = [[0 for i in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
    '''



    # This solution is more optimized for space, we store a n*2
    # matrix, hence O(n) space
	'''
	dp = [[0 for _ in range(len(text2)+1)] for _ in range(2)]

	for i in range(len(text1)-1, -1, -1):
		for j in range(len(text2)-1, -1, -1):
			dp[0][j] = 1+dp[1][j+1] if text1[i] == text2[j] else max(dp[1][j], dp[0][j+1])
		dp[0], dp[1] = dp[1], dp[0] 
	return dp[1][0]
	'''


	# In this solution, we only use a 1-d stack , and we keep track of three important values:
	# the value that should have been below the current cell in iteration, the one that should
	# have been beside it to the right, and the one that should have been diagonal to it.
	# note that these variables store the values that should have been in the relative positions 
	# to the current cell in iteration in the original n*m matrix.

	dp = [0 for _ in range(len(text2)+1)]
	diag = 0
	for i in range(len(text1)-1, -1, -1):
		for j in range(len(text2)-1, -1, -1):
			if text1[i]==text2[j]:
				tmp = dp[j]
				dp[j] = 1+diag
				diag = tmp
			else:
				diag = dp[j]
				dp[j] = max(dp[j+1], dp[j])
	return dp[0]

			

print(longestCommonSubsequence('abcde', 'abcf'))