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


tree1 = TreeNode(
	val = 2,
	left=TreeNode(1),
	right = TreeNode(3)
)
#           2
#         /   \
#        1     3
print(kthSmallest(tree1, 2))




tree2 = TreeNode(
	val=6,
	left=TreeNode(
		val=2, 
		left=TreeNode(0),
		right=TreeNode(
			val=4,
			left=TreeNode(3),
			right=TreeNode(5)
		)
	),
	right=TreeNode(
		val=8, 
		left=TreeNode(7),
		right=TreeNode(9)
	)
)
#             6
#           /   \
#         2       8
#        / \     / \
#       0   4   7   9
#          / \
#         3   5
print(kthSmallest(tree2, 5))