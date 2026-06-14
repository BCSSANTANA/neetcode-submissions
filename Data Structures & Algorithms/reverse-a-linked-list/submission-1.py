class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        res = ListNode(head.val)
        nextNode = head.next
        while nextNode:
            temp = ListNode(nextNode.val, res)
            nextNode = nextNode.next
            res = temp
        return res
        
        