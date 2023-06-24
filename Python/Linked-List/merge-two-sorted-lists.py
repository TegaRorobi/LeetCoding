# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"



def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # out_lst = []; out_nodes = None
    # while list1:
    #     out_lst.append(list1.val)
    #     list1 = list1.next
    # while list2:
    #     out_lst.append(list2.val)
    #     list2 = list2.next 
    # for i in sorted(out_lst)[::-1]:
    #     out_nodes = ListNode(i, out_nodes)
    # return out_nodes


    dummy = curr = ListNode()
    # print(f"Curr: {str(curr):45s}, Dummy: {dummy}\n\n") 

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            curr, list1 = list1, list1.next
            # print(f"Curr: {str(curr):45s}, Dummy: {dummy}\n\n") 
        else:
            curr.next = list2
            curr, list2 = list2, list2.next
            # print(f"Curr: {str(curr):45s}, Dummy: {dummy}\n\n") 
    if list1 or list2:
        curr.next = list1 if list1 else list2 
    
    return dummy.next 



l1 = ListNode(1, ListNode(3, ListNode(4, None)))
l2 = ListNode(1, ListNode(2, ListNode(4, None)))
print(mergeTwoLists(l1, l2))