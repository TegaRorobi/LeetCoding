# a preorder traversal is just bfs..

# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        # return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        return f"{self.val}"


def preorderTraversal(root):
	return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right) if root else []

def preorderTraversal2(root):
	ans = []
	def dfs(node):
		ans.append(node.val)
		if node.left:
			dfs(node.left)
		if node.right:
			dfs(node.right)
	if root:
		dfs(root)
	return ans 


# vanilla iterative dfs
def preorderTraversal_Iterative(root):
	stack = [root]
	ans = []
	while stack:
		node = stack.pop()
		ans.append(node.val)
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)
	return ans


tree = TreeNode(
	val=1,
	left=TreeNode(
		val=2,
		left=TreeNode(
			val=3),
		right=TreeNode(
			val=4),
	),
	right=TreeNode(
		val=5
	)
)

#       1
#     /   \
#    2     5
#   /  \     
#  3    4


print(preorderTraversal(tree))
print(preorderTraversal2(tree))
print(preorderTraversal_Iterative(tree))
