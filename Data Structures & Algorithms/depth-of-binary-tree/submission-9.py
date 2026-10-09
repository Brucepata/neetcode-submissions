# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if node:
            return 1 + max(get_depth(node.left), get_depth(node.right))
        else:
            return 0

            
            

            

        