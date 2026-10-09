# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if  (root.left and root.left.val >= root.val )or (root.right and root.right.val <= root.val):
            return False 
        return self.is_valid_helper(root.left) and self.is_valid_helper(root.right)
        

    
    def is_valid_helper(self, node: Optional[TreeNode]):
        if not node:
            return True
        if (node.left and node.left.val >= node.val )or (node.right and node.right.val <= node.val):
            return False 
        return self.is_valid_helper(node.left) and self.is_valid_helper(node.right)
        