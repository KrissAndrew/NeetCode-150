import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import unittest
from Python_NeetCode_150.Easy.Problem_2_Best_Time_to_Buy_and_Sell_Stock.solutions import maxProfit

class TestStockPurchase(unittest.TestCase):
        
        def test_buy_sell_stock(self):
            print("\nRunning tests for 'Best Time to Buy and Sell Stock'")

            # Test case 1
            self.stock_data_1 = [10, 3, 7, 4, 1] # 4 (3 - 7)
            self.assertEqual(maxProfit(self.stock_data_1), 4)

            # Test case 2
            self.stock_data_2 = [1, 2, 3, 4, 5, 6] # 5 (6 - 1)
            self.assertEqual(maxProfit(self.stock_data_2), 5)
            
            
            # Test case 3
            self.stock_data_3 = [1, 2] # 1
            self.assertEqual(maxProfit(self.stock_data_3), 1)

            # Test case 4
            self.stock_data_4 = []
            self.assertEqual(maxProfit(self.stock_data_4), 0)

            # Test case 5 - Single
            self.stock_data_5 = [5]
            self.assertEqual(maxProfit(self.stock_data_5), 0)


if __name__ == '__main__':
    unittest.main()