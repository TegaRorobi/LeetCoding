class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"


class MyHashSet:
	def __init__(self):
		self.stack = [ListNode() for _ in range(10000)]

	def add(self, number:int) -> None:
		ind = number % 10000
		curr = self.stack[ind]
		while curr.next:
			curr = curr.next 
		curr.next = ListNode(number)

	def remove(self, number:int) -> None:
		ind = number % 10000
		curr = self.stack[ind]
		while curr.next:
			if curr.next.val == number:
				curr.next = curr.next.next

	def contains(self, number:int) -> bool:
		ind = number % 10000
		curr = self.stack[ind]
		while curr.next:
			if curr.next.val == number:
				return True 
		return False


h = MyHashSet()
h.add(7)
h.add(10007)
h.add(20007)
h.remove(5)
print(h.contains(12))
print(h.contains(7))
