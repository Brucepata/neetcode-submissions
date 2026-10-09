class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False  # Empty list cannot have a cycle

        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # If slow and fast meet, there's a cycle

        return False  # If while loop completes without finding a cycle, return False
