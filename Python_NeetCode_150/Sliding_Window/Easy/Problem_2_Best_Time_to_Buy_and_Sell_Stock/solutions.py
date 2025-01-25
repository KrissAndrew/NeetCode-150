from typing import List

def maxProfit(prices: List[int]) -> int:
    if not prices : return 0 # Empty list

    lowest = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - lowest)
        if price < lowest:
            lowest = price
    return max_profit