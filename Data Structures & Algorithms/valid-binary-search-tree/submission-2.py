# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_helper(root.left, root) and self.is_valid_helper(root.right, root)
        

    
    def is_valid_helper(self, node: Optional[TreeNode], parent_node: Optional[TreeNode]):
        if not node:
            return True
        if node and node.val >= parent_node.val:
            return False
        if node and node.val <= parent_node.val:
            return False
        return self.is_valid_helper(parent_node.left, parent_node) and self.is_valid_helper(parent_node.right, parent_node)
        