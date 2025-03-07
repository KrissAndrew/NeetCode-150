import unittest
from .solutions import *

class TestContainerWithMostWater(unittest.TestCase):
        
    test_cases = [
        # ([], 0),                    # 1: Empty list.
        # ([0], 0),                   # 2: Zero height.
        # ([0, 0], 0),                # 3: Multiple zero heights
        # ([1, 1], 1),                # 4: Minimum height and distance.
        # ([1, 1, 1], 2),             # 5: Minimum height greater distance
        # ([2, 2, 2], 4),             # 6: Multiple zeros produce a single triplet.                         
        ([0,2,0,3,1,0,1,3,2,1], 9), # 7: More complex example.
    ]

    def test_container_with_most_water(self):
        print("\nRunning tests for 'Three Sum'")
        for idx, (numbers, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(test=idx):
                result = trapping_rain_water(numbers)
                self.assertEqual(
                    result, expected,
                    f"Test case {idx} failed: numbers={numbers}, expected={expected} but got {result}"
                )

if __name__ == '__main__':
    unittest.main()
