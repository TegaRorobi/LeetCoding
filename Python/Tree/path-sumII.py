# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        
def pathSum(root:TreeNode, targetSum:int) -> list[list[int]]:
    if not root:
        return []
    stack, res = [(root, root.val, [root.val])], []
    while stack:
        node, curr_sum, path = stack.pop()
        if curr_sum==targetSum and not node.left and not node.right:
            res.append(path)
        if node.right:
            stack.append((node.right, curr_sum+node.right.val, path+[node.right.val]))
        if node.left:
            stack.append((node.left, curr_sum+node.left.val, path+[node.left.val]))
    return res


def pathSum2(root:TreeNode, targetSum:int) -> list[list[int]]:
    res = []
    def dfs(node, curr_sum, path):
        if not node:
            return None 
        if curr_sum+node.val == targetSum and not node.left and not node.right:
            res.append(path+[node.val])
        dfs(node.left, curr_sum+node.val, path+[node.val])
        dfs(node.right, curr_sum+node.val, path+[node.val])
    dfs(root, 0, [])
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

print(pathSum(tree, 10))
print(pathSum2(tree, 10))