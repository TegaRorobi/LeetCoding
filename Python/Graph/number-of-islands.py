#Medium

# my solution
def numIslands(grid):
	if not grid:
		return 0 

	rows = len(grid)
	cols = len(grid[0])
	
	visited = set()
	def explore(r, c):
		visited.add((r, c))
		if  grid[r][c] == "1":
			directions = [(0,-1), (-1,0), (1,0), (0,1)]
			for dr, dc in directions:
				r1 = r+dr
				c1 = c+dc
				if -1<r1<rows and -1<c1<cols and (r1, c1) not in visited:
					visited.add((r1, c1))
					explore(r1, c1)

	num_islands = 0
	for r in range(rows):
		for c in range(cols):
			if (r, c) not in visited and grid[r][c] == '1':
				num_islands += 1
				explore(r, c)
	return num_islands

# bfs solution with a deque
def numIslandsBFS(grid):
	if not grid: return 0

	rows = len(grid)
	cols = len(grid[0])
	visited = set()

	from collections import deque
	def bfs(r, c):
		queue = deque([(r, c)])
		while queue:
			r, c = queue.popleft()
			if -1<r<rows and -1<c<cols and grid[r][c] == '1' and (r, c) not in visited:
				queue.append((r+1, c)) # exploring the bottom
				queue.append((r, c+1)) # exploring the right
				queue.append((r-1, c)) # exploring the top
				queue.append((r, c-1)) # exploring the left
			visited.add((r, c))

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

grid3 = [
	["1", "1", "1"],
	["0", "1", "0"],
	["1", "1", "1"]
]

grid4 = [
	["1", "1", "1", "1", "0"],
	["1", "1", "0", "1", "0"],
	["1", "1", "0", "0", "0"],
	["0", "0", "0", "0", "0"]
]

print(numIslands(grid1))
print(numIslands(grid2))
print(numIslands(grid3))
print(numIslands(grid4))
