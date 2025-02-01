import unittest
from .solutions import *

class TestEncodeDecodeStrings(unittest.TestCase):

        test_cases = [
            ([[""], '#0#']),
            (["Two", "Words"], '#3#Two#5#Words'),
            (["2", "Words"], '#1#2#5#Words'),
        ]
        
        def test_encode_decode_strings(self):
            print("\nRunning tests for 'Encode Decode Strings'")
            for encode_decode_args in self.test_cases:
                with self.subTest(encode_decode_args=encode_decode_args):
                     self.assertEqual(encode_strings(encode_decode_args[0]), encode_decode_args[1])
                     self.assertEqual(decode_strings(encode_decode_args[1]), encode_decode_args[0])

if __name__ == '__main__':
    unittest.main()
