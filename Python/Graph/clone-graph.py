# MEDIUM

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not none else []

def cloneGraph(node:Node) -> Node:
	hashmap = {}

	def clone(node):
		if node in hashmap:
			return hashmap[node]

		copy_node = Node(node.val)
		hashmap[node] = copy_node
		for neighbor in node.neighbors:
			copy.neighbors.append(clone(neighbor))

		return copy_node
	return clone(node) if node else Node()
