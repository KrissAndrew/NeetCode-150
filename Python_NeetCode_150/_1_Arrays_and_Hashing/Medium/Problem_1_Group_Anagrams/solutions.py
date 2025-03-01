from collections import defaultdict
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# O(n)
def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list) # A default dict initialises new keys without errors

    strs = [word.lower() for word in strs]

    for word in strs:
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        # The tuple of char counts is used as the key as opposed to a list as it is immutable
        # the value is a list of the words that match that tuple
        anagram_map[tuple(char_count)].append(word) 

    return list(anagram_map.values())