
# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

# FIFO, recursive dfs
def maxDepth(root:TreeNode) -> int:
	return 1+max(maxDepth(root.left), maxDepth(root.right)) if root else 0


# FIFO
# this algorithm visits the nodes in a pre-order fashion
def maxDepth_iterative_dfs(root:TreeNode) -> int:
	if not root: return 0
	res = 0
	stack = [(root, 1)]
	while stack:
		node, level = stack.pop()
		# print(node.val)
		res = max(level, res)
		if node.right:
			stack.append((node.right, level+1))
		if node.left:
			stack.append((node.left, level+1))
	# print('-----')
	return res

# LIFO
def maxDepth_bfs(root:TreeNode) -> int:
	if not root: return 0
	from collections import deque
	queue = deque([root])
	depth = 0
	while queue:
		for _ in range(len(queue)):
			node = queue.popleft()
			# print(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		depth += 1
	# print('----')
	return depth

def maxDepth_bfs2(root: TreeNode) -> int:
	if not root: return 0
	from collections import deque
	res = 0
	q = deque([(root, 1)])
	while q:
		node, depth = q.popleft()
		# print(node.val)
		res = max(res, depth)
		if node.left:
			q.append((node.left, 1+depth))
		if node.right:
			q.append((node.right, 1+depth))
	# print('----')
	return res




tree = TreeNode(
	val=9, 
	left=TreeNode(
		val=20, 
		left=TreeNode(
			val=23,
			left=TreeNode(
				val=42)), 
		right=TreeNode(
			val=31,)
	), 
	right=TreeNode(
		val=15,
		right=TreeNode(
			val=18))
	)
#           9
#         /   \
#       20     15
#      /  \      \
#     23  31      18
#    /
#   42

print(maxDepth(tree))
print(maxDepth_iterative_dfs(tree))
print(maxDepth_bfs(tree))
print(maxDepth_bfs2(tree))
