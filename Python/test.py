
# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"



def sumNodeDepths(root):
	res = 0
	stack = [(root, 0)]
	while stack:
		node, depth = stack.pop()
		res += depth 
		if node.right:
			stack.append((node.right, depth+1))
		if node.left:
			stack.append((node.left, depth+1))
	return res

# this solution is not optimal, all i need for the result is an integer and
# since I can't pass in the integer by reference like in C or C++, and since
# integers are immutable and strings are so I am just appending the number of
# times the original integer should be there
'''
def sumNodeDepths_recursive(root):
	res = []
	def dfs(node, depth):
		if node.left:
			res.extend([0]*(depth+1))
			dfs(node.left, depth+1)
		if node.right:
			res.extend([0]*(depth+1))
			dfs(node.right, depth+1)
	dfs(root, 0)
	return len(res)
'''


def sumNodeDepthsBFS(root):
	from collections import deque
	res = 0
	q = deque([(root, 0)])
	while q:
		node, level = q.popleft()
		res += level
		if node.left:
			q.append((node.left, level+1))
		if node.right:
			q.append((node.right, level+1))
	return res


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


print(sumNodeDepths_recursive(tree))
print(sumNodeDepths(tree))
print(sumNodeDepthsBFS(tree))
