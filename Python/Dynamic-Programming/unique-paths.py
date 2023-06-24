
def uniquePaths(m:int, n:int) -> int:

	# runtime and space complexities assume:
	# m is the number of rows of the matrix
	# n is the number of columns of the matrix.

	# O(m*n) runtime, O(n*m) space
	# matrix = [[0 for i in range(n+1)] for i in range(m+1)]
	# matrix[-2][-2] = 1

	# for r in range(m-1, -1, -1):
	# 	for c in range(n-1, -1, -1):
	# 		if matrix[r][c] == 0:
	# 			matrix[r][c] = matrix[r][c+1] + matrix[r+1][c] #+ matrix[r+1][c+1]
	# return matrix[0][0]



	# O(m*n) runtime, O(n) space
	# dp = [0] * (n-1) + [1, 0]
	dp = [1] * n
	# for row in range(m):
	for row in range(m-1):
		# for col in range(n-1, -1, -1):
		for col in range(n-2, -1, -1):
			dp[col] = dp[col+1] + dp[col]
	return dp[0]



'''
______________________
|Go|  |  |  |  |  |  |
----------------------
|  |  |  |  |  |  |  |
----------------------
|  |  |  |  |  |  |$$|
----------------------
'''

print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(1, 1))
