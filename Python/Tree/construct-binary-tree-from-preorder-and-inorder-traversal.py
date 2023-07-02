
# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


def buildTree(preorder:list[int], inorder:list[int]) -> TreeNode:
	if not preorder or not inorder:
		return None
	# the first value in a preorder traversal is always the root node.
	root = TreeNode(preorder[0])
	head = inorder.index(preorder[0])

	root.left = buildTree(preorder[1:head+1], inorder[:head])
	root.right = buildTree(preorder[head+1:], inorder[head+1:])
	return root


print(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
print(buildTree([4, 3, 7, 1, 13, 15, 18, 10, 11, 2, 5], [1, 7, 15, 13, 18, 3, 10, 4, 2, 11, 5]))