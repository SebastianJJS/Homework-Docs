"""
Question 5: ShortestSubstring
Given a string and a second string representing required characters, return the length of
the shortest substring containing all the required characters.

Time Complexity: O(n), it uses a sliding window and each character is processed at most twice
Space Complexity: O(1), the character frequency map has at most 26 entries

Technique:
Sliding window with frequency map.

Approach:
Use two pointers to maintain a window containing all required characters. Expand the
right pointer to include characters until all required ones are present. Then, move
the left pointer inward to minimize the substring while maintaining all characters.
Repeat until the shortest valid substring is found.
"""

# Time: 37 min

import pytest
from collections import Counter

def shortest_substring(s, required):
    required_counts = Counter(required)
    window_counts = Counter()
    left, matched = 0, 0
    min_length = float("inf")

    for right, char in enumerate(s):
        window_counts[char] += 1
        if char in required_counts and window_counts[char] == required_counts[char]:
            matched += 1

        while matched == len(required_counts):
            min_length = min(min_length, right - left + 1)
            window_counts[s[left]] -= 1
            if s[left] in required_counts and window_counts[s[left]] < required_counts[s[left]]:
                matched -= 1
            left += 1

    return min_length if min_length != float("inf") else -1

@pytest.mark.parametrize("s, required, expected", [
    ("abracadabra", "abc", 4),
    ("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx", 10),
    ("dog", "god", 3),
    ("aabbcc", "abc", 4),
    ("abcdef", "xyz", -1),
    ("abacbdab", "abd", 3),
    ("", "", -1),
    ("a", "a", 1),
    ("abcdefg", "gfedcbaa", -1),
    ("abcdabcda", "abcdabcda", 9)
])

def test_shortest_substring(s, required, expected):
    assert shortest_substring(s, required) == expected