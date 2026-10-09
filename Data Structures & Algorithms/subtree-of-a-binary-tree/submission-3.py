# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_same_tree(self, node1, node2):
        if node1.val == node2.val:
            return self.is_same_tree(node1.left, node2.left) and self.is_same_tree(node2.right, node2.right)   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot or not root:
            return False
        if root.val == subRoot.val:
            return self.isSubtree(root, subRoot)
        return self.isSubtree(root.left, subRoot.left) or self.isSubtree(root.right, subRoot.right)

        
       