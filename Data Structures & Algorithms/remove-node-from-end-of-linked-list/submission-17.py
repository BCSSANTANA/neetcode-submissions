# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevSlow = None
        slow = head
        fast = head
        sz = 1

        if not head.next:
            return None
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
            sz += 2
        if not fast:
            sz -= 1
        
        pos = sz // 2 + 1
        d1 = (sz - n) + 1 - pos
        d2 = (sz - n) + 1 - 1
    
        
        if d1 <= d2 and d1 >= 0:
            i = 0
            while i < d1:
                prevSlow = slow
                slow = slow.next
                i += 1
            
            if prevSlow:
                prevSlow.next = slow.next
            else: 
                if slow.next:
                    slow = slow.next
                else:
                    return None
        else:
            i = 0
            prevHead = None
            it = head
            while i < d2:
                prevHead = it
                it = it.next
                i += 1
            if prevHead:
                prevHead.next = it.next
            else:
                return it.next

        return head