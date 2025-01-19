import unittest
from Python_NeetCode_150.Common.Binary_Tree import *
from Solution import tree_is_balanced

class TestTreeBalance(unittest.TestCase):
        
        def setUp(self):
            # Prepare some sample trees for testing
            self.tree_data_1 = [1, 2, 3, None, None, 4, 5]
            self.tree_data_2 = [1, 2, 3, 4, None, None, None]
            self.tree_data_3 = [1, 2, None]
            
            # Creating tree nodes from the sample data
            self.root_1 = create_tree_from_list(self.tree_data_1)
            self.root_2 = create_tree_from_list(self.tree_data_2)
            self.root_3 = create_tree_from_list(self.tree_data_3)

        def test_tree_is_balanced(self):
              self.assertTrue(tree_is_balanced(self.root_1))
              self.assertFalse(tree_is_balanced(self.root_2))
              self.assertTrue(tree_is_balanced(self.root_3))

if __name__ == '__main__':
    unittest.main()