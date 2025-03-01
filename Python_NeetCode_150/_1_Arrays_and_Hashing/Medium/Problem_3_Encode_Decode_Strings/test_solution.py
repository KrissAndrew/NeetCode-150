import unittest
from .solutions import encode_strings, decode_strings

class TestEncodeDecodeStrings(unittest.TestCase):

    # Test cases for encode_strings:
    # Each tuple: (input list of strings, expected encoded string)
    encode_test_cases = [
        ([""], "#0#"),
        (["Two", "Words"], "#3#Two#5#Words"),
        (["2", "Words"], "#1#2#5#Words"),
        (["#1#", "#1#", "#1#", "#1#", "#1#"], "#3##1##3##1##3##1##3##1##3##1#"),
    ]

    # Test cases for decode_strings:
    # Each tuple: (encoded string, expected list of strings)
    decode_test_cases = [
        ("#0#", [""]),
        ("#3#Two#5#Words", ["Two", "Words"]),
        ("#1#2#5#Words", ["2", "Words"]),
        ("#3##1##3##1##3##1##3##1##3##1#", ["#1#", "#1#", "#1#", "#1#", "#1#"]),
    ]
    
    def test_encode_strings(self):
        print("\nRunning tests for 'Encode Strings'")
        for idx, (strings, expected) in enumerate(self.encode_test_cases, start=1):
            with self.subTest(test=idx):
                result = encode_strings(strings)
                self.assertEqual(
                    result, expected,
                    f"Test encode case {idx} failed: strings={strings}, expected={expected} but got {result}"
                )
    
    def test_decode_strings(self):
        print("\nRunning tests for 'Decode Strings'")
        for idx, (encoded, expected) in enumerate(self.decode_test_cases, start=1):
            with self.subTest(test=idx):
                result = decode_strings(encoded)
                self.assertEqual(
                    result, expected,
                    f"Test decode case {idx} failed: encoded={encoded}, expected={expected} but got {result}"
                )

if __name__ == '__main__':
    unittest.main()
