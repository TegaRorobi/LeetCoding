# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"


# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
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

# a binary search tree
tree = TreeNode(
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


# A Node i.e in a graph
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not none else []
        

# A trie node i.e from word search II
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        cur = self 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


# a trie's separate class dictnode
class DictNode:
    isWord = False
    children = {}
    
# the actual trie
class Trie:
    def __init__(self):
        self.root = DictNode
    def addWord(self, word):
        curr = self.root 
        for char in word:
            if char not in curr.children:
                curr.children[char] = DictNode()
            curr = curr.children[char]
        curr.isWord = True