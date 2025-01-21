from typing import List

def maxProfit(prices: List[int]) -> int:
    
    lowest = prices[0]
    daily_profit = 0
    max_profit = 0

    for price in prices[1:]:
        daily_profit = price - lowest
        if daily_profit > max_profit: max_profit = daily_profit
        if price < lowest:
            lowest = price

    return max_profit

if __name__ == '__main__':
    test = [10, 3, 7, 4, 1] # Expected out come is 4
    print(maxProfit(test))

