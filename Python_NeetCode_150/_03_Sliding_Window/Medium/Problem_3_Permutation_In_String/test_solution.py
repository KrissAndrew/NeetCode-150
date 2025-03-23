# import unittest
# from .solutions import permutation_in_string

# class TestPermutationInString(unittest.TestCase):

#     test_cases = [
#         (("ABC", 1), 2),     #  1 - Can replace one for "(AA)C"|"A(BB)"|"A(CC)" = len 3
#         (("ABA", 1), 3),     #  1 - Can replace one for "(AAA)" = len 3
#         (("XYYX", 1), 3),    #  1 - Can replace one for "X(YYY)"|"(YYY)X" = len 3
#         (("XYYX", 2), 4),    #  1 - Can replace two for "(XXXX)" = len 4
#         (("AAABABB", 1), 5), #  2 - Can replace one for "(AAAAA)BB" = len 5
#         (("AAABABB", 2), 6), #  2 - Can replace Two for "(AAAAAA)B" = len 6
#     ]

#     def test_longest_repeat_char_replacement(self):
#         print("\nRunning tests for 'Best Time to Buy and Sell Stock'")
#         for idx, (input, expected) in enumerate(self.test_cases, start=1):
#             with self.subTest(test=idx):
#                 result = permutation_in_string(*input)
#                 self.assertEqual(
#                     result, expected,
#                     f"Test case {idx} failed: input={input}, expected={expected} but got {result}"
#                 )

# if __name__ == '__main__':
#     unittest.main()
