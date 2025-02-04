from typing import List

# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

# O(n^2)
def product_except_self_blind(nums: List[int]) -> List[int]:
    result = [0] * len(nums)
    i = 0
    while i < len(nums):
        product = 1
        j = 0
        while j < len(nums):
            if j != i: product *= nums[j]
            j += 1
        result[i] = product
        i += 1
    
    return result

# O(n)
def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    prefix = 1
    suffix = 1

    # Compute prefix products
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Compute suffix products and multiply with prefix results
    for i in range(n - 1, -1, -1): # for i in [3, 2, 1, 0]
        result[i] *= suffix
        suffix *= nums[i]

    return result

if __name__ == "__main__":
    Input = [1,2,4,6]
    Output = [48,24,12,8]
    print(f"Expected: {Output} | Result: {product_except_self(Input)}")
