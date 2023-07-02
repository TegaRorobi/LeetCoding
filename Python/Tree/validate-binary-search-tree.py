# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        # return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        return f"{self.val}"


def isValidBST(root) -> bool:
	if not root:
		return False
	stack = [(root, [2**31], [2**-31])]
	while stack:
		node, lt, gt = stack.pop()
		if node.val < min(lt) and node.val > max(gt):
			if node.right:
				stack.append((node.right, lt, gt+[node.val]))
			if node.left:
				stack.append((node.left, lt+[node.val], gt))
		else:
			return False
	return True


# iterative dfs traversal, keeping track of the least value each node in the stack has to be less than
# and also keeping track of the greatest value each node in the stack has to be greater than for the 
# tree to be valid.
def isValidBST2(root) -> bool:
	if not root:
		return False
	stack = [(root, 2**31, 2**-31)]
	while stack:
		node, lt, gt = stack.pop()
		if node.val < lt and node.val > gt:
			if node.right:
				stack.append((node.right, lt, max(gt,node.val)))
			if node.left:
				stack.append((node.left, min(lt,node.val), gt))
		else:
			return False
	return True

# iterative in-order traversal, each value has to be less than the previous value we encountered
# default is negative infinity
def isValidBST3(root) -> bool:
	if not root:
		return False
	stack = []
	prev = float("-inf")
	while stack or root:
		if root:
			stack.append(root)
			root = root.left 
		else:
			node = stack.pop()
			if node.val <= prev:
				return False
			prev = node.val
			root = node.right 
	return True



tree1 = TreeNode(
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
tree2 = TreeNode(
	val = 2,
	left=TreeNode(
		val=1),
	right = TreeNode(
		val=3)
	)
#           2
#         /   \
#        1     3
tree3 = TreeNode(
	val=5,
	left=TreeNode(
		val=4),
	right=TreeNode(
		val=6,
		left=TreeNode(
			val=3),
		right=TreeNode(
			val=7)
		)
	)
#           5
#         /   \
#        4     6
#            /   \
#           3     7

print(isValidBST3(tree1))
print(isValidBST3(tree2))
print(isValidBST3(tree3))