# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        # return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        return f"{self.val}"


def kthSmallest(root: TreeNode, k: int) -> int:
    found, stack = 0, [root]
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            found += 1
            if found == k:
                return node.val
            root = node.right


tree = TreeNode(
	val = 2,
	left=TreeNode(
		val=1),
	right = TreeNode(
		val=3)
	)

print(kthSmallest(tree, 2))