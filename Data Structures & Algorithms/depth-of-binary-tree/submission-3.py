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
            elif node:
                return prevd+1
            
            return max(get_max(node.left, prevd), get_max(node.right, prevd))            

        return max(get_max(root.left,1), get_max(root.right,1))
        