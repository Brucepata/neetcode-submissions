class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head

        dummyNode = ListNode(0, head)

        left = dummyNode

        while(n > 0):
            right = right.next
            n -= 1

        print("headval is ", head.val)
        
        while(right):
            right = right.next
            left = left.next
        

        left.next = left.next.next

        return dummyNode.next

        

