from Python_NeetCode_150.Common.Binary_Tree import *
from typing import Optional

def tree_is_balanced(self, root: Optional[TreeNode]) -> bool:
    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)