# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def get_depth(node, curDepth):

            if node:
                return 1 + max(get_depth(node.left, curDepth), get_depth(node.right, curDepth))
            else:
                return 0
        
        return max(get_depth(root.left,0), get_depth(root.right,0))
            
            

            

        