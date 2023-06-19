def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
	if obstacleGrid[-1][-1] == 1:
		return 0
	else:
		obstacleGrid[-1][-1] = 1

	n_rows = len(obstacleGrid)
	n_cols = len(obstacleGrid[0])

	obstacleGrid.append([0 for _ in range(n_cols+1)])
	

	for r in range(n_rows-1, -1, -1):
		obstacleGrid[r].append(0)
		for c in range(n_cols-1, -1, -1):

			if r==n_rows-1 and c==n_cols-1: continue

			if obstacleGrid[r][c] == 1: 
				obstacleGrid[r][c] = 0; continue

			obstacleGrid[r][c] = obstacleGrid[r][c+1] + obstacleGrid[r+1][c]

	return obstacleGrid[0][0]



print(uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(uniquePathsWithObstacles(obstacleGrid = [[0,1],[0,0]]))
print(uniquePathsWithObstacles(obstacleGrid = [[0,0],[0,1]]))
print(uniquePathsWithObstacles(obstacleGrid = [[1]]))
