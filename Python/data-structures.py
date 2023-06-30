# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"


# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        
# a sample tree
tree = TreeNode(
    val=9, 
    left=TreeNode(
        val=20, 
        left=TreeNode(
            val=23,
            left=TreeNode(
                val=42)), 
        right=TreeNode(
            val=31,)
    ), 
    right=TreeNode(
        val=15,
        right=TreeNode(
            val=18))
    )

#           9
#         /   \
#       20     15
#      /  \      \
#     23  31      18
#    /
#   42

# A Node i.e in a graph
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not none else []
        