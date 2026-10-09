class Solution:
    def is_same_tree(self, p, q):
        # If both nodes are null, trees are identical at this position
        if not p and not q:
            return True
        # If one is null or values differ, trees are not identical
        if not p or not q or p.val != q.val:
            return False
        # Recursively check left and right children
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # A null subRoot is technically a subtree of any tree
        if not subRoot: return True
        # If the main tree is exhausted but subRoot isn't, no match
        if not root: return False
        
        # 1. Check if the trees are identical starting at the current node
        if self.is_same_tree(root, subRoot):
            return True
        
        # 2. Otherwise, check if subRoot exists in the left or right children
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
