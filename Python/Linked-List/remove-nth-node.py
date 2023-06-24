
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"



def removeNthNode(head:ListNode, n:int) -> ListNode:
	dummy = ListNode(0, head)
	left, right = dummy, head

	for _ in range(n):
		right = right.next 
		
	while right:
		left, right = left.next, right.next 
	left.next = left.next.next
	return dummy.next 


listnode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(removeNthNode(listnode, 2))
