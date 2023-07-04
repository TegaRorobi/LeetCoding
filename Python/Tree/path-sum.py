# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        
def hasPathSum(root:TreeNode, targetSum:int) -> bool:
    if not root:
        return False 
    stack = [(root, root.val)]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == targetSum:
            return True
        if node.right:
            stack.append((node.right, curr_sum+node.right.val))
        if node.left:
            stack.append((node.left, curr_sum+node.left.val))
    return False

# a recursive solution
def hasPathSum2(root:TreeNode, targetSum:int) -> bool:

    def dfs(node, curr_sum):
        if not node:
            return False
        if curr_sum+node.val == targetSum and not node.left and not node.right:
            return True 
        return (dfs(node.left, curr_sum+node.val) or
                dfs(node.right, curr_sum+node.val))
    return dfs(root, 0)

# a sample tree
tree = TreeNode(
    val=5, 
    left=TreeNode(
        val=1, 
        left=TreeNode(
            val=2,
            left=TreeNode(
                val=7)), 
        right=TreeNode(
            val=4,)
    ), 
    right=TreeNode(
        val=3,
        right=TreeNode(
            val=9))
    )

#           5
#         /   \
#       1       3
#      /  \      \
#     2   4       9
#    /
#   7

print(hasPathSum(tree, 17))
print(hasPathSum2(tree, 17))