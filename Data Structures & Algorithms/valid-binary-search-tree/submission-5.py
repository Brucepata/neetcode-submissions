# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
TODO: Need to set an upper bound and lower bound while traversing 

'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_helper(root, float('-inf'), float('inf'))
    
    def is_valid_helper(self, node: Optional[TreeNode], lower_bound, upper_bound) -> bool:
        if not node:
            return True
        
        # Check if current node violates bounds
        if not (lower_bound < node.val < upper_bound):
            return False
        
        # Left subtree: upper bound becomes node.val
        left_valid = self.is_valid_helper(node.left, lower_bound, node.val)
        
        # Right subtree: lower bound becomes node.val
        right_valid = self.is_valid_helper(node.right, node.val, upper_bound)
        
        return left_valid and right_valid
        