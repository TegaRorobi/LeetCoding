# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


# using a deque, intuitive solution, and we can print out the deque to view the path
def pathSum(root: TreeNode, targetSum: int) -> int:
    if not root:
        return 0
    res = 0
    from collections import deque
    stack = [(root, deque([root.val]), root.val)]
    while stack:
        node, path, sum_ = stack.pop()
        check, prev_sum = path.copy(), sum_
        while check:
            if sum_ == targetSum:
                # print(check)
                res += 1
                break
            sum_ -= check.popleft()
        if node.right:
            stack.append((node.right, path+deque([node.right.val]), prev_sum+node.right.val))
        if node.left:
            stack.append((node.left, path+deque([node.left.val]), prev_sum+node.left.val))
    return res


# removed the overhead of importing and using a deque
def pathSum2(root: TreeNode, targetSum: int) -> int:
    """
    Time complexity:
        I visit every node in the tree while I run the iterative dfs => O(n)
        and then for every node I visit, I check all the numbers i traversed to get to that node => O(logn)
        Therefore, this algorighm has an algorithm of O(nlogn) for a balanced tree and O(n^2) in the 
        worst case where n is equal to the height of the tree.
    """
    res = 0
    stack = [(root, [root.val], root.val)]
    while stack:
        node, path, sum_ = stack.pop()
        curr_sum = sum_ 
        for num in path:
            if sum_ == targetSum:
                res += 1
                if num != 0:
                    break
            sum_ -= num
        if node.right:
            stack.append((node.right, path+[node.right.val], curr_sum+node.right.val))
        if node.left:
            stack.append((node.left, path+[node.left.val], curr_sum+node.left.val))
    return res


# recursive solution
def pathSum3(root: TreeNode, targetSum: int) -> int:
    res = 0
    def dfs(node, curr, path):
        curr_sum = curr 
        for num in path:
            if curr == targetSum:
                nonlocal res 
                res += 1
            curr -= num 
        if node.left: 
            dfs(node.left, curr_sum+node.left.val, path+[node.left.val])
        if node.right: 
            dfs(node.right, curr_sum+node.right.val, path+[node.right.val])
    if root:
        dfs(root, root.val, [root.val])
    return res



tree = TreeNode(
    val=10,
    left = TreeNode(
        val=5,
        left=TreeNode(
            val=3,
            left=TreeNode(3),
            right=TreeNode(-2)
        ),
        right=TreeNode(
            val=2,
            right=TreeNode(1)
        ),
    ),
    right = TreeNode(
        val=-3,
        right=TreeNode(11)
    )
)
#           10
#          /   \
#        5      -3
#      /   \      \
#     3     2      11
#    / \     \   
#   3  -2     1

tree2 = TreeNode(
    val=0, 
    left=TreeNode(1),
    right=TreeNode(1)
)
print(pathSum3(tree, 8))
print(pathSum3(tree, 7))
print(pathSum3(tree2, 1))