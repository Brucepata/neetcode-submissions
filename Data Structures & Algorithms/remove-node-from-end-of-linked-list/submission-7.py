class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        while(n > 0):
            right = right.next
            n -= 1
        
        while(right):
            right = right.next
            left = left.next
        

        left.next = left.next.next
        return head

        

