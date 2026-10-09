# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        while(head.next and head.next.next):
            slow = head.next
            fast = head.next.next

            if slow == fast:
                return False
            
        
        return True


        