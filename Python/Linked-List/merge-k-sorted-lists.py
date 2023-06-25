# Hard

from merge_two_sorted_lists import mergeTwoLists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

def mergeKLists(lists: list[ListNode]) -> ListNode:
    # edge case
    if not lists:
        return None 
    'while the lists variable hasn\'t been completely merged, we break it up'
    'into adjacent pairs of 2 and merge them together and store these merged'
    'variables into a new variable (which now has a length of roughly len(lists)/2)'
    'and then we replace the lists variable with this mergedLists variable'

    while len(lists) > 1:
        mergedLists = []
        'breaking the list into adjacent pairs of 2'
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1)<len(lists) else None #edge case for odd number of lists

            'instead of writing out again, i\'ll just use the already written function that'
            'merges two lists as it is the exact same process.'
            mergedLists.append(mergeTwoLists(l1, l2))
        lists = mergedLists
    return lists[0]


lists = [
    ListNode(5, ListNode(9)), 
    ListNode(3, ListNode(6, ListNode(12))), 
    ListNode(8), 
    ListNode(2, ListNode(4, ListNode(4)))
]
print(mergeKLists(lists))