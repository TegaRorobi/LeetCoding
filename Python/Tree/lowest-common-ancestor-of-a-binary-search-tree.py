# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        # return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
        return f"{self.val}"


# initial solution
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    p, q = min(p.val, q.val), max(p.val, q.val)
    stack = [root]
    while stack:
        node = stack.pop()
        # taking advantage of the fact that it's a binary search tree
        if p <= node.val and q >= node.val:
            return node

        # eliminate the right, p and q are located to the left of this node
        if p < node.val and q < node.val:
            stack.append(node.left)

        # conversely, eliminate the left as p and q are located to the right of this node
        if p > node.val and q > node.val:
            stack.append(node.right)
                    

# simplification and refactoring
""" we first identify the smaller and larger treenode of p and q, and 
then we continue eliminating half of the tree until either:
i.) p is the root node and q, being greater is to the right of it
ii.) q is the root node and q, being less is to the left of it.
iii.) p is to the left of the root node and q is to the right of the root node.

So while this condition is not satisfied, we check that if even the 
smallest value p is to the right of the current root node, 
then p,being greater is also to the right and hence they are both on the right.
If this is not satisfied still, then p and q must definitely be to the left
of the current root node. Therefore, we shift our pointers accordingly.
"""
def lowestCommonAncestor2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	p, q = sorted([p.val, q.val])
	while not p <= root.val <= p:
		root = (root.left, root.right)[p>root.val] 
	return root

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

print(lowestCommonAncestor(tree, TreeNode(2), TreeNode(4)))
print(lowestCommonAncestor2(tree, TreeNode(2), TreeNode(4)))
