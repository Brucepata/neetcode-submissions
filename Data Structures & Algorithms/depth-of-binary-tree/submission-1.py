# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def get_max(node, prevd):
            if not node:
                return prevd
            if node:
                return prevd+1
            
            return max(get_max(node.left, prevd), get_max(node.right, prevd))            

        return get_max(root,0)
        