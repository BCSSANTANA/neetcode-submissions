# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        val = head.val
        head.val = (1, val)
        head = head.next
        while head:
            if isinstance(head.val, tuple):
                return True
            val = head.val
            head.val = (1, val)
            head = head.next
        return False