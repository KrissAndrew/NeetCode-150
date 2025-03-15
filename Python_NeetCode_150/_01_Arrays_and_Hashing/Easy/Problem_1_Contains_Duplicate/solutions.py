def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen: return True
        seen.add(num)
    return False

def contains_duplicate_one_line(nums: list[int]) -> bool:
    return (len(set) < len(nums))