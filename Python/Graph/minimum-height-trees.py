# medium

# recursive
def getMaxHeight(node, adj, visit):
	if not adj[node] or node in visit:
		return 0 
	height = 0
	visit.add(node)
	for neigh in adj[node]:
		height = max(height, getMaxHeight(neigh, adj, visit))
	return 1 + height

#iterative
def getMaxHeight2(node, adj):
	stack, res = [(node, 0)], 0
	vis = set()
	while stack:
		node, level = stack.pop()
		vis.add(node)
		res = max(res, level)
		for node in adj[node]:
			if node not in vis:
				stack.append([node, level+1])
	return res



# O(n^2) time complexity, because we check each node, 
# and then for each stop we run a dfs to check the maximum depth
# in which we also visit all the nodes from that node.
# The space complexity is roughly O(n),  the adjacency list takes O(n)
# and the stack in the dfs function is also O(n).
def findMinHeightTrees(n:int, edges:list[list[int]]) -> list[int]:
	adj = {key:[] for key in range(n)}
	for u, v in edges:
		adj[u].append(v)
		adj[v].append(u)

	mht, res = 2*10**4, []
	for node in range(n):
		maxH = getMaxHeight2(node, adj)

		if maxH == mht:
			res.append(node) 
		elif maxH < mht:
			mht, res = maxH, [node]
	return res




def findMinHeightTrees2(n:int, edges:(list[list[int]])) -> list[int]:
	if n < 3:
		return edges[0] if n==2 else [0]

	adj = {key:[] for key in range(n)}
	for u, v in edges:
		adj[u].append(v)
		adj[v].append(u)

	mht, res = 2*10**4, []
	for node in range(n):
		if len(adj[node]) > 1 :
			maxH = getMaxHeight2(node, adj)

			if maxH == mht:
				res.append(node) 
			elif maxH < mht:
				mht, res = maxH, [node]
	return res

	res = []
	for key in adj:
		if len(adj[key]) > 1:
			res.append(key)
	return res
    

# Extremely clever solution, eat up all the leaves until we have one 
# or two nodes left, O(n) runtime and space complexity 👌🙌
def findMinHeightTrees3(n:int, edges:list[list[int]]) -> list[int]:
	if n==1:
		return [0]

	adj = [set() for _ in range(n)]
	for u, v in edges:
		adj[u].add(v)
		adj[v].add(u)

	leaves = [i for i in range(n) if len(adj[i]) == 1]
	while n>2:
		n -= len(leaves)
		newLeaves = []
		for leaf in leaves:
			branch = adj[leaf].pop()
			adj[branch].remove(leaf)
			if len(adj[branch]) == 1:
				newLeaves.append(branch)
		leaves = newLeaves
	return leaves



print(findMinHeightTrees3(4, [[1,0],[1,2],[1,3]]))
print(findMinHeightTrees3(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
