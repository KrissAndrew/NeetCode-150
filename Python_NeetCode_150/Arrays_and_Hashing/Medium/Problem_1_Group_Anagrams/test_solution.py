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
            for anagrams, expected in self.test_cases:
                with self.subTest(anagrams=anagrams):
                     self.assertEqual(group_anagrams(anagrams), expected)
                 

if __name__ == '__main__':
    unittest.main()
