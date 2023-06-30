# A binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


def isSameTree(p, q) -> bool:
	stackp, stackq = [p], [q]
	while stackp and stackq:
		p, q = stackp.pop(), stackq.pop()
		if p == None and q == None:
			continue
		if (q==None or p==None) or (p.val != q.val):
			return False
		stackp.extend((p.right, p.left))
		stackq.extend((q.right, q.left))
	if stackp or stackq:
		return False
	return True


print(isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))
print(isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))))
print(isSameTree(TreeNode(1, TreeNode(2), None), TreeNode(1, None, TreeNode(2))))