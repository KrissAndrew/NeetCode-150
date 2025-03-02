import unittest
from .binary_tree import create_tree_from_list
from .solutions import tree_is_balanced_recursive, tree_is_balanced_iterative

class TestTreeBalance(unittest.TestCase):
    
    # Each tuple: (tree_data as a list, expected balanced result)
    test_cases = [
        ([1, 2, 3, None, None, 4, 5], True),        # 1 - Balanced tree
        ([1, 2, 3, None, None, 4, None, 5], False), # 2 - Unbalanced tree
        ([1, 2, None], True),                       # 3 - Balanced tree (only left child)
        ([], True),                                 # 4 - Empty tree is balanced
    ]
        
    def test_tree_is_balanced(self):
        print("\nRunning tests for 'Tree is Balanced'")
        for idx, (tree_data, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(test=idx):
                root = create_tree_from_list(tree_data)
                result_recursive = tree_is_balanced_recursive(root)
                result_iterative = tree_is_balanced_iterative(root)
                self.assertEqual(
                    result_recursive, expected,
                    f"Test case {idx} failed (recursive): tree_data={tree_data}, expected={expected} but got {result_recursive}"
                )
                self.assertEqual(
                    result_iterative, expected,
                    f"Test case {idx} failed (iterative): tree_data={tree_data}, expected={expected} but got {result_iterative}"
                )

if __name__ == '__main__':
    unittest.main()
