
def exist1(board:list[list[int]], word:str) -> bool:
	rows, cols = len(board), len(board[0])
	visited = set()

	def dfs(r, c, pos):
		if not ((r, c) not in visited and -1<r<rows and -1<c<cols and board[r][c] == word[pos]):
			return False
		if pos == len(word)-1: 
			return True 

		visited.add((r, c))
		found = dfs(r+1, c, pos+1) or dfs(r-1, c, pos+1) or dfs(r, c+1, pos+1) or dfs(r, c-1, pos+1)
		visited.remove((r, c))
		return found


	for r in range(len(board)):
		for c in range(len(board[0])):
			if board[r][c] == word[0] and (r, c) not in visited:
				if dfs(r, c, 0):
					return True
	return False



# we don't need a visited set
def exist2(board:list[list[str]], word:str) -> bool:
	rows, cols = len(board), len(board[0])
	# just found out the 'nonlocal' keyword in python... :(
	found = False
	def dfs(r, c, pos):
		if pos == len(word)-1: 
			nonlocal found
			found = True 
			return

		directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
		for dr, dc in directions:
			r1, c1 = r+dr, c+dc
			if -1<r1<rows and -1<c1<cols and board[r1][c1] == word[pos+1]:
				board[r1][c1] = '#'
				dfs(r1, c1, pos+1)
				board[r1][c1] = word[pos+1]


	for r in range(len(board)):
		for c in range(len(board[0])):
			if board[r][c] == word[0]:
				board[r][c] = '#'
				dfs(r, c, 0)
				board[r][c] = word[0]
	return found




def exist(board:list[list[str]], word:str) -> bool:
	rows, cols = len(board), len(board[0])

	def dfs(r, c, i):
		if i==len(word)-1:
			return True 
		paths = []
		for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
			r1, c1 = r+dr, c+dc
			if -1<r1<rows and -1<c1<cols and board[r1][c1]==word[i+1]:
				original_value = board[r1][c1]
				board[r1][c1] = '#'
				paths.append(dfs(r1, c1, i+1))
				board[r1][c1] = original_value
		return any(paths)

	for r in range(len(board)):
		for c in range(len(board[0])):
			if board[r][c] == word[0]:
				board[r][c] = '#'
				if dfs(r, c, 0):
					return True
				board[r][c] = word[0]
	return False




board1 = [
	['A', 'B', 'C', 'E'], 
	['S', 'F', 'C', 'S'], 
	['A', 'D', 'E', 'E']
]

board2 = [
	['X', 'T', 'N', 'O'], 
	['A', 'E', 'M', 'H'], 
	['A', 'G', 'E', 'T'], 
	['E', 'R', 'A', 'R']
]
print(exist2(board1, "ABCCED"))
print(exist2(board2, "RARE"))