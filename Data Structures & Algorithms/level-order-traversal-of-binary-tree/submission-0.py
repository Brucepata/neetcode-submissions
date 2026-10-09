from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        
        cur_stack = deque([])
        cur_stack.append(root)

        while cur_stack:
            cur_level = []
            for i in range(len(cur_stack)):
                popper = cur_stack.popleft()
                cur_level.append(popper.val)
                if popper.left:
                    cur_stack.append(popper.left)
                if popper.right:
                    cur_stack.append(popper.right)
            if cur_level:
                ans.append(cur_level)
        
        return ans

        