# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val == subRoot.val:
            return is_same_tree(root, subRoot)
        return is_same_tree(root.left, subRoot.left) or is_same_tree(root.right, subRoot.right)

        
        def is_same_tree(node1, node2):
            if node1.val == node2.val:
                return is_same_tree(node1.left, node2.left) and is_same_tree(node2.right, node2.right)