from typing import List
from collections import defaultdict

# Given an integer array nums and an integer k, return the k most frequent elements within the array.

def most_frequent_elements_blind(nums: List[int], element_count: int) -> List[int]:
    if not nums: return []
    freq_counts = defaultdict(int) # A default dict initialises new keys without key errors
    most_frequent_keys = []

    for num in nums:
        freq_counts[num] += 1

    for _ in range(element_count):
        max_key = max(freq_counts, key=freq_counts.get)
        most_frequent_keys.append(max_key)
        freq_counts.pop(max_key)

    return most_frequent_keys

from collections import Counter
import heapq

def most_frequent_elements(nums: List[int], element_count: int) -> List[int]:
    # Count freq of each element
    freq_counts = Counter(nums) # O(n)

    # Use a heap to find top k elements
    most_frequent_keys = heapq.nlargest(element_count, freq_counts.keys(), key=freq_counts.get)

    return most_frequent_keys
