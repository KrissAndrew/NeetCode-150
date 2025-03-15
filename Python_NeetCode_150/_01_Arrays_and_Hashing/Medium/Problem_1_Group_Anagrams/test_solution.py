import unittest
from .solutions import *

class TestGroupAnagrams(unittest.TestCase):

        test_cases = [
            (["cat", "act", "map", "amp", "dog", "god"], [["cat", "act"], ["map", "amp"], ["dog", "god"]]),
            (["Cat", "act", "MAp", "amp", "DOG", "god"], [["cat", "act"], ["map", "amp"], ["dog", "god"]]),
            (["a"], [["a"]]),
            (["Cat", "MAp", "DOG"], [["cat"], ["map"], ["dog"]])
        ]
        
        def test_group_anagrams(self):
            print("\nRunning tests for 'Group Anagrams'")
            for idx, (words, expected) in enumerate(self.test_cases, start=1):
                with self.subTest(test=idx):
                    result = group_anagrams(words)
                    self.assertEqual(
                        result, expected,
                        f"Test case {idx} failed: words={words}, expected={expected} but got {result}"
                    )

if __name__ == '__main__':
    unittest.main()
