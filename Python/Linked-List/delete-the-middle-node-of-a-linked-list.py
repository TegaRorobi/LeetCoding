

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

def deleteMiddle(head: ListNode):
	slow, fast = head, head.next.next

	# if there's one node in the head
	if not fast:
	    return None

	# finding the node before the middle of the head node
	# the fast pointer traverses twice as fast as the slow pointer
	while fast and fast.next:
	    slow, fast = slow.next, fast.next.next

	# deleting the node
	slow.next = slow.next.next

	# head is also modified
	return head


listnode1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
listnode2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
listnode3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(deleteMiddle(listnode1))
print(deleteMiddle(listnode2))
print(deleteMiddle(listnode3))