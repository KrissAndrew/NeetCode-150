import sys
import os

# Explicitly add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Diagnostic print statements
print(f"Current working directory: {os.getcwd()}")
print(f"Current sys.path: {sys.path}")

from Python_NeetCode_150.Common.binary_tree import *
from typing import Optional

def tree_is_balanced_recursive(root: Optional[TreeNode]) -> bool:
    def height(node):
        if not node:
            return 0
        
        # Recursively get the heights of the left and right subtrees
        left_height = height(node.left)
        right_height = height(node.right)

        # If either subtree is unbalanced, propagate -1 upwards
        if left_height == -1 or right_height == -1:
            return -1
        
        # If the height difference is more than 1, mark this node as unbalanced
        if abs(left_height - right_height) > 1:
            return -1
        
        # Return the height of the current node
        return 1 + max(left_height, right_height)
    
    # The tree is balanced if the height of the root is not -1
    return height(root) != -1


   
def tree_is_balanced_iterative(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    
    stack = [] # To perform post-order traversal
    height_map = {} # To store the heights of subtrees

    # Push the root onto the stack with a visited flag
    stack.append((root, False))

    while stack:
        node, visited = stack.pop()

        if node is None:
            continue

        if visited:
            # Post-order processing: compute height
            left_height = height_map.get(node.left, 0)
            right_height = height_map.get(node.right, 0)

            # Check if the current node is balanced
            if abs(left_height - right_height) > 1:
                return False  # Tree is unbalanced

            # Store the height of the current node
            height_map[node] = 1 + max(left_height, right_height)
        else:
            stack.append((node, True))

            # Push children for processing
            stack.append((node.right, False))
            stack.append((node.left, False))
    
    return True # If no imbalance is found, the tree is balanced




