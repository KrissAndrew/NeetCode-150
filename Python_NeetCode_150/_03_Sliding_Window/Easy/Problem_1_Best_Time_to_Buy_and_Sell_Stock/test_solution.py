import unittest
from .solutions import max_profit

class TestStockPurchase(unittest.TestCase):

    test_cases = [
        ([10, 3, 7, 4, 1], 4),       # max profit is 7 - 3 = 4
        ([1, 2, 3, 4, 5, 6], 5),     # max profit is 6 - 1 = 5
        ([1, 2], 1),                 # max profit is 2 - 1 = 1
        ([], 0),                     # empty list returns 0 profit
        ([5], 0),                    # single element returns 0 profit
    ]
        
    def test_buy_sell_stock(self):
        print("\nRunning tests for 'Best Time to Buy and Sell Stock'")
        for idx, (stock_data, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(test=idx):
                result = max_profit(stock_data)
                self.assertEqual(
                    result, expected,
                    f"Test case {idx} failed: stock_data={stock_data}, expected={expected} but got {result}"
                )

if __name__ == '__main__':
    unittest.main()
