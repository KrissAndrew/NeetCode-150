import sys
import os

# Explicitly add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Diagnostic print statements
print(f"Current working directory: {os.getcwd()}")
print(f"Current sys.path: {sys.path}")

import unittest
from Python_NeetCode_150.Common.binary_tree import create_tree_from_list
from Python_NeetCode_150.Easy.Problem_1_Balanced_Binary_Tree.solutions import tree_is_balanced_recursive, tree_is_balanced_iterative

class TestTreeBalance(unittest.TestCase):
        
        def test_tree_is_balanced(self):
            print("\nRunning tests for 'tree is balanced'")

            # Test case 1 - Balanced Tree
            self.tree_data_1 = [1, 2, 3, None, None, 4, 5]
            self.root_1 = create_tree_from_list(self.tree_data_1)
            self.assertTrue(tree_is_balanced_recursive(self.root_1))
            self.assertTrue(tree_is_balanced_iterative(self.root_1))

            # Test case 2 - Unbalanced Tree
            self.tree_data_2 = [1, 2, 3, None, None, 4, None, 5]
            self.root_2 = create_tree_from_list(self.tree_data_2)
            self.assertFalse(tree_is_balanced_recursive(self.root_2))
            self.assertFalse(tree_is_balanced_iterative(self.root_2))
            
            # Test case 3 - Balanced Tree
            self.tree_data_3 = [1, 2, None]
            self.root_3 = create_tree_from_list(self.tree_data_3)
            self.assertTrue(tree_is_balanced_recursive(self.root_3))
            self.assertTrue(tree_is_balanced_iterative(self.root_3))

            # Test case 4 - Balanced Tree
            self.tree_data_4 = []
            self.root_4 = create_tree_from_list(self.tree_data_4)
            self.assertTrue(tree_is_balanced_recursive(self.root_4))
            self.assertTrue(tree_is_balanced_iterative(self.root_4))

if __name__ == '__main__':
    unittest.main()
