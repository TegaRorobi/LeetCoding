class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

def levelOrder(root: TreeNode) -> list[list[int]]:
    from collections import deque
    if not root:
        return []
    res = []
    stack = deque([root])
    while stack:
        res.append([])
        for _ in range(len(stack)):
            node = stack.popleft()
            res[-1].append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return res


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


print(levelOrder(tree))