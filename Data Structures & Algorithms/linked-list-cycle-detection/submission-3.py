# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow = head

        while(slow and slow.next):
            fast = slow.next.next

            if slow == fast:
                return False
            
            slow = slow.next         
        
        return True


        