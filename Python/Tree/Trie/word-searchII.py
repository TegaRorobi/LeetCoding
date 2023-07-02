
class TrieNode:
	def __init__(self):
		self.children = {}
		self.isWord = False
	def addWord(self, word):
		cur = self 
		for c in word:
			if c not in cur.children:
				cur.children[c] = TrieNode()
			cur = cur.children[c]
		cur.isWord = True
	def __repr__(self):
		return f"TrieNode(children={list(self.children.keys())}, isWord={self.isWord})"

def findWords(board:list[list[str]], words:list[str]) -> list[str]:
	root = TrieNode()
	for w in words: 
		root.addWord(w)


	rows, cols = len(board), len(board[0])
	res, visited = set(), set()

	def dfs(r, c, node, word):
		if r<0 or c<0 or r==rows or c==cols or board[r][c] not in node.children or (r, c) in visited:
			return

		node = node.children[board[r][c]]
		word += board[r][c]
		if node.isWord:
			res.add(word)

		visited.add((r, c))
		for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
			dfs(r+dr, c+dc, node, word)
		visited.remove((r, c))

	for r in range(rows):
		for c in range(cols):
			dfs(r, c, root, "")

	return list(res)

board = [
	['o', 'a', 'a', 'n'],
	['e', 't', 'a', 'e'],
	['i', 'h', 'k', 'r'],
	['i', 'f', 'l', 'v'],
]
words = ['oath', 'pea', 'eat', 'rain']
print(findWords(board, words))