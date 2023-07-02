# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


# Iterative solution
# the idea is to traverse the root array in a normal iterative dfs fashion, and
# if at any point the value at the current node is equal to the value of the head
# node of the subRoot, then we want to perform sameTree on those two nodes.
# if it fails, we are still free to try out other nodes in the root node.
# runtime was pretty high, but the memory is efficient.

# on leetcode, this runtime beats only 5%, but the memory beats over 99%
def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
	stack1 = [root]
	while stack1:
		node = stack1.pop()
		# check if they are the same tree
		if node.val == subRoot.val:
			stack, sub_stack = [node], [subRoot]
			while stack and sub_stack:
				node1, node2 = stack.pop(), sub_stack.pop()
				if not node1 and not node2: continue
				if not node1 or not node2:  break
				if node1.val == node2.val:
					stack.extend((node1.right, node1.left))
					sub_stack.extend((node2.right, node2.left))
				else:
					break
			if not stack and not sub_stack and node1==node2: 
				return True

		if node.right: stack1.append(node.right)
		if node.left:  stack1.append(node.left)
	return False




# recursive solution
# on leetcode, the runtime of this solution beats 17%, but the memory beats 9%
def isSubtree2(root: TreeNode, subRoot: TreeNode) -> bool:
	# this is a leetcode problem solution by itself
	def isSame(a, b):
		if a is None and b is None:
			return True 
		if a is None or b is None or a.val!=b.val:
			return False 
		return isSame(a.left, b.left) and isSame(a.right, b.right)

	if not root: 
		return root==subRoot
	if isSame(root, subRoot):
		return True 
	return isSubtree2(root.left, subRoot) or isSubtree2(root.right, subRoot)



tree1 = TreeNode(val=1, left=TreeNode(1))
tree2 = TreeNode(1)
print(isSubtree2(tree1, tree2))


tree3 = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
tree4 = TreeNode(val=1, left=TreeNode(2))
print(isSubtree2(tree3, tree4))


tree5 = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
tree6 = None
print(isSubtree2(tree5, tree6))
