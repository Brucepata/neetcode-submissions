# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_val = float("-inf")

        if not root:
            return 0 

        self.dfs(root)

        return self.max_val 

    def dfs(self, node):
        if not node:
            return 0
        elif not node.right and not node.left:
            return node.val
        
        self.max_val = max(self.max_val,self.dfs(node.left), node.val, self.dfs(node.right))

        return self.max_val

        