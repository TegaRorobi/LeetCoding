

class Graph:
	def __init__(self, n_vertices):
		self.__adj = {key:[] for key in range(n_vertices)}
		self.__n_vertices = n_vertices


	def addEdge(self, u, v):
		self.__adj[u].append(v)


	def topologicalSort_util(self, node, visited, stack):
		visited.add(node)
		for nxt in self.__adj[node]:
			if nxt not in visited:
				self.topologicalSort_util(nxt, visited, stack)
		stack.append(node)
		

	def topologicalSort(self):
		stack = []
		visited = set()
		for node in range(self.__n_vertices):
			if node not in visited:
				self.topologicalSort_util(node, visited, stack)
		return stack[::-1]



g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.topologicalSort())
