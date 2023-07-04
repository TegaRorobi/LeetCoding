# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


def binaryTreePaths(root: TreeNode) -> list[str]:
    if not root: return [""]
    stack, res = [(root, str(root.val))], []
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            res.append(path)
        if node.right:
            stack.append((node.right, f"{path}->{node.right.val}"))
        if node.left:
            stack.append((node.left, f"{path}->{node.left.val}"))
    return res



# a sample tree
tree = TreeNode(
    val=5, 
    left=TreeNode(
        val=1, 
        left=TreeNode(
            val=3,
            left=TreeNode(
                val=1)), 
        right=TreeNode(
            val=4,)
    ), 
    right=TreeNode(
        val=3,
        right=TreeNode(
            val=2))
    )

#           5
#         /   \
#       1       3
#      /  \      \
#     3    4       2
#    /
#   1

print(binaryTreePaths(tree))