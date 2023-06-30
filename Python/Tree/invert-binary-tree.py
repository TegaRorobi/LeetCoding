class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


def invertTree(root: TreeNode) ->TreeNode:
    if 	not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

def invertTree_Iterative(root: TreeNode) -> TreeNode:
	if not root:
		return None 
	stack = [root]
	while stack:
		node = stack.pop()
		node.left, node.right = node.right, node.left 
		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)
	return root

tree = TreeNode(
	val=1,
	left = TreeNode(
		val = 2, 
		left=TreeNode(4),
		right=TreeNode(5),
	),
	right=TreeNode(
		val=3, 
		left=TreeNode(6),
		right=TreeNode(7),
	),
)

print(invertTree_Iterative(tree))
print(invertTree(tree))