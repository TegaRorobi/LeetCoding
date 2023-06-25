#Medium

# my solution
def numIslands(grid):
	if not grid:
		return 0 

	rows = len(grid)
	cols = len(grid[0])
	
	visited = set()
	def explore(x, y):
		if (x, y) not in visited and x<rows and y<cols and grid[x][y] == '1':
			# explore the coordinate to the right and then mark it
			explore(x+1, y)
			visited.add((x+1, y))

			# explore the coordinate to the bottom and then mark it
			explore(x, y+1)
			visited.add((x, y+1))

	num_islands = 0
	for r in range(rows):
		for c in range(cols):
			if (r, c) not in visited and grid[r][c] == '1':
				num_islands += 1
				explore(r, c)
	return num_islands

# bfs solution with a deque
def numIslandsBFS(grid):
	if not grid:
		return 0

	rows = len(grid)
	cols = len(grid[0])
	visited = set()

	from collections import deque
	def bfs(x, y):
		queue = deque([(x, y)])
		while queue:
			x, y = queue.popleft()
			if x<rows and y<cols and grid[x][y] == '1' and (x, y) not in visited:
				queue.append((x+1, y))
				queue.append((x, y+1))
			visited.add((x, y))

	num_islands = 0
	for r in range(rows):
		for c in range(cols):
			if (r, c) not in visited and grid[r][c] == '1':
				num_islands += 1
				bfs(r, c)
	return num_islands


grid1 = [
	['1', '1', '1', '0', '0'],
	['1', '1', '0', '0', '0'],
	['1', '1', '0', '0', '0'],
	['0', '0', '0', '1', '1']
]

grid2 = [
	['1', '1', '1', '0', '1'],
	['1', '1', '0', '1', '0'],
	['1', '0', '1', '0', '0'],
	['0', '0', '0', '1', '1'],
	['0', '0', '0', '1', '1']
]

print(numIslands(grid1))
print(numIslandsBFS(grid2))