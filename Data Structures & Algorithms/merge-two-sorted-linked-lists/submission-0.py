# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iterable1 = list1
        iterable2 = list2
        dummy = ListNode()
        res = dummy
        while iterable1 or iterable2:
            if iterable1 and iterable2:
                if iterable1.val <= iterable2.val:
                    res.next = ListNode(iterable1.val)
                    iterable1 = iterable1.next
                else:
                    res.next = ListNode(iterable2.val)
                    iterable2 = iterable2.next
            elif iterable1:
                res.next = ListNode(iterable1.val)
                iterable1 = iterable1.next
            elif iterable2:
                res.next = ListNode(iterable2.val)
                iterable2 = iterable2.next
            res = res.next
        return dummy.next