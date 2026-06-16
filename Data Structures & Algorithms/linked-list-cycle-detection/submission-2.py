class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortoise = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True
        return False