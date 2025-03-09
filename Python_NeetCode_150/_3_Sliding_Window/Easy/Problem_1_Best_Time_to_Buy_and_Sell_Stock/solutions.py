def max_profit(prices: list[int]) -> int:
    if not prices or len(prices) < 2:
        return 0 # Empty list
    
    lowest = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - lowest)
        if price < lowest:
            lowest = price

    return max_profit

if __name__ == "__main__":
    test_cases = [
        ([10, 3, 7, 4, 1], 4),       # max profit is 7 - 3 = 4
        ([1, 2, 3, 4, 5, 6], 5),     # max profit is 6 - 1 = 5
        ([1, 2], 1),                 # max profit is 2 - 1 = 1
        ([3,2,6,5,0,3], 3),
        ([], 0),                     # empty list returns 0 profit
        ([5], 0),                    # single element returns 0 profit
    ]
    for array, expected in test_cases:
        print(max_profit(array))