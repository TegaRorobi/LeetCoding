# for a postorder binary tree traversal, for ANY given node, 
# all the parent nodes are processed first, usually left then right
# before that node. therefore the first node to be procesed is the 
# leftmost node in relation to the root node and the last node to be
# processed is the root node.


# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        # return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        return f"{self.val}"


def postorderTraversal(root):
	return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val] if root else []

def postorderTraversal2(root):
	res = []
	def dfs(node):
		if node.left:
			dfs(node.left)
		if node.right:
			dfs(node.right)
		res.append(node.val)
	if root:
		dfs(root)
	return res

# my first working solution after trying to figure out the iterative solution
def postorderTraversal_Iterative(root):
	stack = []
	ans = []
	processed = []
	while True:
		while root:
			stack.append(root)
			root = root.left 
		if not stack:
			return ans 
		node = stack.pop()
		if node.right and node.right not in processed:
			stack.append(node)
			processed.append(node.right)
			root = node.right
		else:
			ans.append(node.val)

# now refactoring...
# we don't need a whole processed array, we can store a boolean along with each node on the stack.
def postorderTraversal_Iterative2(root):
	stack = []
	ans = []
	while True:
		while root:
			stack.append((root, False))
			root = root.left 

		if not stack:
			return ans 

		node, done_right = stack.pop()
		if node.right and not done_right:
			stack.append((node, True)) # so we can visit it again and append its value
			root = node.right # explore that node
		else:
			# this means we're revisiting the node or perhaps the node has no children
			ans.append(node.val)


# just for good measure... :)
def postorderTraversal_Iterative3(root):
	stack, ans = [], []
	while stack or root:
		if root:
			stack.append((root, False))
			root = root.left 
		else:
			node, done_with_right = stack.pop()
			if node.right and not done_with_right:
				stack.append((node, True))
				root = node.right 
			else:
				ans.append(node.val)
	return ans

tree = TreeNode(
	val=5,
	left=TreeNode(
		val=3,
		left=TreeNode(
			val=1),
		right=TreeNode(
			val=2),
	),
	right=TreeNode(
		val=4
	)
)

#       5
#     /   \
#    3     4
#   /  \     
#  1    2


print(postorderTraversal(tree))
print(postorderTraversal2(tree))
print(postorderTraversal_Iterative(tree))
print(postorderTraversal_Iterative2(tree))
print(postorderTraversal_Iterative3(tree))