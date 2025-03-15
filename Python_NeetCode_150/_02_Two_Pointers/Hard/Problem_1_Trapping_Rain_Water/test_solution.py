import unittest
from .solutions import *

class TestContainerWithMostWater(unittest.TestCase):
        
    test_cases = [
        ([], 0),                        #  1: Empty list.
        ([0], 0),                       #  2: Zero height.
        ([0, 0], 0),                    #  3: Multiple zero heights, less than 3 heights.
        ([1, 1, 1], 0),                 #  4: Even heights.
        ([1, 0, 1], 1),                 #  5: Simplest case.
        ([0, 1, 0, 1, 0], 1),           #  6: Add outer values - increase complexity.                         
        ([1, 0, 1, 0 , 1], 2),          #  7: Increase complexity.                         
        ([0,2,0,3,1,0,1,3,2,1], 9),     #  8: More complex example.
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6), #  9: More complex example.
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
