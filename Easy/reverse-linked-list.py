
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"


def reverseList_Iterative(head:ListNode) -> ListNode:
	'O(n) runtime O(1) space'
	curr = head 
	prev = None
	while curr:
		temp = curr.next 
		curr.next = prev 
		prev = curr 
		curr = temp
	return prev


def reverseList_Recursive(head:ListNode) -> ListNode:
	'O(n) runtime and O(n) space'
	# as of now, I don't really understand how this works -_-
	def rev(node):
		new_node = node 
		if node.next:
			new_node = rev(node.next)
			node.next.next= node 
		node.next = None 
		return new_node
	return rev(head)

 
listnode =  ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
listnode2 =  ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(reverseList_Iterative(listnode))
# print(reverseList_Recursive(listnode2))


# 1 -> 2 -> 3 -> 4 -> 5
