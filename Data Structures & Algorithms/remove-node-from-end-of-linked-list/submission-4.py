# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # given example 4, we need to remove 3. 
        # which means we need to move len() - n times 
        if not head:
            return head

        ll_len = 0

        counter = head

        while(counter):
            ll_len += 0 
            counter = counter.next
        
        to_move = ll_len - n

        tracker = head

        for i in range(to_move-2):
            tracker = tracker.next
        
        if tracker.next:
            tracker.next = tracker.next.next
        else:
            tracker.next = None
            
        return head
