import unittest
from .binary_tree import *
from .solutions import tree_is_balanced_recursive, tree_is_balanced_iterative

class TestTreeBalance(unittest.TestCase):
        
        def test_tree_is_balanced(self):
            print("\nRunning tests for 'Tree is Balanced'")

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
