# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


def maxPathSum(root:TreeNode) -> int:
    res = root.val

    def dfs(node):
        if not node:
            return 0 

        leftMax = max(dfs(node.left), 0)
        rightMax = max(dfs(node.right), 0)

        # recording the possibility that we just take the left and right max and 
        # split at this node 
        nonlocal res 
        res = max(res, node.val+leftMax+rightMax)

        # returning the value without a split to be used by the parent node 
        return node.val + max(leftMax, rightMax)

    dfs(root)
    return res

tree = TreeNode(
    val=4, 
    left=TreeNode(
        val=2, 
        left=TreeNode(
            val=13,
            left=TreeNode(
                val=-2)), 
        right=TreeNode(
            val=6,)
    ), 
    right=TreeNode(
        val=15,
        right=TreeNode(
            val=-5))
    )

#           4
#         /   \
#        2     15
#      /  \      \
#     13   6      -5
#    /
#   -2

print(maxPathSum(tree))