# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out_lst = []; out_nodes = None
        
        while list1:
            out_lst.append(list1.val)
            list1 = list1.next
        while list2:
            out_lst.append(list2.val)
            list2 = list2.next 
        
        for i in sorted(out_lst)[::-1]:
            out_nodes = ListNode(i, out_nodes)
        return out_nodes
        

        ### Previous buggy, disgraceful and slow tries

        # lst1,lst2 = [], []
        # def unpack(listnode, to_list):
            # to_list.append(listnode.val)
            # if listnode.next == None: return 
            # return unpack(listnode.next, to_list)

        # unpack each input listnode into a variable
        # unpack(list1, lst1); unpack(list2, lst2)

        # join the listnodes together and sort
        # ans_lst = sorted(lst1 + lst2)

        # def repack(val_lst):
            # if len(val_lst) == 1:
                # return ListNode(val_lst[0], None)
            # return ListNode(val_lst[0], repack(val_lst[1:]))
        
        # pack the resulting list into a variable
        # nodes = repack(ans_lst)

        # return the variable
        # print(nodes)