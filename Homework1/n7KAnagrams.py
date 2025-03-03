"""
Question 7: KAnagrams
Two strings are considered to be “k-anagrams” if they can be made into anagrams by
changing at most k characters in one of the strings. Given two strings and an integer k,
determine if they are k-anagrams.

Time Complexity: O(n), we traverse the strings
Space Complexity: O(1), since we store at most 26 character frequencies

Technique:
Hashmap count

Approach:
Count character frequencies for both strings using hashmaps. Check if their lengths match;
if not, return False. Compute the total differences by subtracting one frequency count
from the other. Compare the required changes to k and return True if within the limit;
otherwise, return False.
"""

# Time: 16 min

import pytest
from collections import Counter


def k_anagrams(s1, s2, k):
    if len(s1) != len(s2):
        return False

    freq1 = Counter(s1)
    freq2 = Counter(s2)

    diff_count = 0

    for char in freq1:
        if char in freq2:
            diff_count += max(0, freq1[char] - freq2[char])
        else:
            diff_count += freq1[char]

    return diff_count <= k

@pytest.mark.parametrize("s1, s2, k, expected", [
    ("apple", "peach", 1, False),
    ("apple", "peach", 2, True),
    ("cat", "dog", 3, True),
    ("debit curd", "bad credit", 1, True),
    ("baseball", "basketball", 2, False),
    ("listen", "silent", 0, True),
    ("anagram", "nagaram", 1, True),
    ("hello", "bello", 1, True),
    ("aaaaa", "bbbbb", 5, True),
    ("abcdef", "ghijkl", 6, True),
])

def test_k_anagrams(s1, s2, k, expected):
    assert k_anagrams(s1, s2, k) == expected