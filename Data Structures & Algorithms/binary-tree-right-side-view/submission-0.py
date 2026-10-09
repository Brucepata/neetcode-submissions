from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_queue = deque([])
        right_side_view = []

        if not root:
            return []

        level_queue.append(root)
        
        self.level_helper(right_side_view, level_queue)

        return right_side_view

    def level_helper(self, right_side_view, level_queue) -> None:

        while(level_queue):
            
            right_side_view.append(level_queue[-1].val)

            new_level_queue = []
            for cur_node in level_queue:
                if cur_node.left:
                    new_level_queue.append(cur_node.left)
                if cur_node.right:
                    new_level_queue.append(cur_node.right)
            
            level_queue = new_level_queue
            


            

                