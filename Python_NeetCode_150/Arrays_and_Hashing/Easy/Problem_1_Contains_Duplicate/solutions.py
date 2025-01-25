# O(n) time complexity - the set can look up variables
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen: return True
        seen.add(num)
    return False

# Clever one liner - if the lengths of a set of a list is not equal to the list, the list contains duplicates 
def contains_duplicate_one_line(nums: list[int]) -> bool:
    return (len(set) < len(nums))