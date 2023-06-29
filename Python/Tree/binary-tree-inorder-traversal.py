# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        # return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        return f"{self.val}"

def inorderTraversal(root: TreeNode) -> list[int]:
	return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []


def inorderTraversal2(root: TreeNode) -> list[int]:
	result = []
	def dfs(node):
		if node.left:
			dfs(node.left)
		result.append(node.val)
		if node.right:
			dfs(node.right)
	if root:
		dfs(root)
	return result

def inorderTraversal_Iterative(root: TreeNode) -> list[int]:
	res = []
	stack = []
	while stack or root:
		if root:
			stack.append(root)
			root = root.left 
		else:
			node = stack.pop()
			res.append(node.val)
			root = node.right
	return res


tree = TreeNode(
	val=4,
	left=TreeNode(
		val=2,
		left=TreeNode(
			val=1),
		right=TreeNode(
			val=3),
	),
	right=TreeNode(
		val=5
	)
)

#       4
#     /   \
#    2     5
#   /  \     
#  1    3
print(inorderTraversal_Iterative(tree))
# def dfs(node):
# 	stack = [node]
# 	while stack:
# 		node = stack.pop()
# 		print(node.val)
# 		if node.right:
# 			stack.append(node.right)
# 		if node.left:
# 			stack.append(node.left)
# dfs(tree)