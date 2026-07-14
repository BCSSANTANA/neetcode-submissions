# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        exp = 0
        carry = 0
        it1 = l1
        it2 = l2
        it3 = ListNode()
        s = it3
        carry = None
        while it1 or it2:
            temp = ListNode()
            if it1 and it2:
                temp.val = it1.val + it2.val
                it1 = it1.next
                it2 = it2.next
            elif it1:
                temp.val = it1.val
                it1 = it1.next
            elif it2:
                temp.val = it2.val
                it2 = it2.next
            if carry:
                    temp.val += carry
            if temp.val >= 10:
                carry = 1
                temp.val = temp.val % 10
            else:
                carry = 0
            it3.next = temp
            it3 = it3.next
        if carry > 0:
            it3.next = ListNode(1)
            
        return s.next