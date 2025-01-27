from typing import List
from collections import defaultdict
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


# Implementation works, but is not the most efficient.

# Computing the character count for each word takes 𝑂(𝐿), where L is the average length of a word.
# For N words, this step takes 𝑂(𝑁⋅𝐿)

# For each word, compare char_count with every other word that hasn't been visited.
# Worst case, this is 𝑂(𝑁^2), if all words have unique char_counts and no early stopping.
def char_counter(count_string: str): # O(L)
    counter = [0] * 26
    
    for char in count_string.lower():
        counter[ord(char) - ord('a')] += 1

    return counter

def group_anagrams_blind(strs: List[str]) -> List[List[str]]:
    char_counts = { word: char_counter(word) for word in strs} # O(L)
    grouped_anagrams = []
    visited = set()

    for word, count in char_counts.items(): # O(N)
        if word in visited: # ignore words already assessed
            continue

        group = [word]
        visited.add(word)

        for other_word, other_count, in char_counts.items(): # O(N) - nested within O(N) = O(N^2)
            if other_word not in visited and other_count == count:
                group.append(other_word)
                visited.add(other_word)

        grouped_anagrams.append(group)

    return grouped_anagrams


# O(n)
def group_anagrams(strs: List[str]) -> List[List[str]]:
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