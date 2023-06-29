# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

def reorderList1(head):
	# marking the beginning of the second half of the head node
	slow = head
	fast = head
	while fast:
		slow = slow.next 
		fast = fast.next.next if fast.next else fast.next
	pre = None 

	# reversing the second half
	while slow:
		nxt = slow.next
		# in the first iteration, the slow pointer still points to the 
		# beginning of the second half of input listnode, ans sets it 
		# to none. So we need to later delete that node so that the 
		# head nodes contains only the nodes from the first half of the
		# input and the second node contains only elements from the second half.
		slow.next = pre 
		pre = slow
		slow = nxt 
	# print(head, pre)

	# deleting the last node in the head node
	remover = head 
	while remover.next.next:
		remover = remover.next
	remover.next = None
	# print(head, pre)

	# combining the first and second half
	dummy = curr = ListNode()
	while pre:
		curr.next = head 
		curr = curr.next 
		head = head.next
		curr.next = pre 
		curr = curr.next 
		pre = pre.next
	curr.next = head

	return dummy.next


def reorderList2(head):
	# finding the start of the second half
	slow = head 
	fast = head.next
	while fast and fast.next:
		slow = slow.next 
		fast = fast.next.next
	# the second half starts from slow.next
	second = slow.next 
	# we set slow.next to None since we are done with it.
	# this modifies the head node and makes it that no node in the 
	# first portion is also in the second portion.
	slow.next = None

	# reversing the second half
	prev = None 
	while second:
		nxt = second.next 
		second.next = prev
		prev = second
		second = nxt
	curr = dummy = ListNode()

	# now the first and second portions are in head and prev respectively
	first = head 
	second = prev

	# merging the halves together
	while second:
		curr.next = first 
		curr = curr.next 
		first = first.next 

		curr.next = second 
		curr = curr.next 
		second = second.next 
	curr.next = first if first else None 
	return dummy.next



def reorderList(head):
	slow, fast = head, head.next 
	while fast and fast.next:
		slow, fast = slow.next, fast.next.next
	second = slow.next 
	slow.next = None 
	prev = None 
	while second:
		temp = second.next 
		second.next = prev 
		prev = second 
		second = temp 
	first, second = head, prev 
	# this inserts the values from the second node in between those from the first
	while second:
		temp1, temp2 = first.next, second.next 
		first.next = second 
		second.next = temp1
		first, second = temp1, temp2

	return head

listnode1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
listnode2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reorderList(listnode1))