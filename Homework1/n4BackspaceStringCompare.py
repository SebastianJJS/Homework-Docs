"""
Question 4: BackspaceStringCompare
Given two strings representing series of keystrokes, determine whether the resulting text
is the same. Backspaces are represented by the '#' character so "x#" results in the empty string ("").

Time Complexity: O(n), each character is processed once in a single pass from right to left.
Space Complexity: O(1), no additional data structures are used

Technique:
A two-pointer approach that traverses the strings from right to left

Approach:
Convert both strings into character streams processed from right to left. Use two pointers to
track valid characters, skipping backspaced ones. Compare characters when both pointers land
on valid indices. Move inward until fully processed, then return whether the strings match.
"""

# Time: 31 min

import pytest

def backspace_string_compare(s1, s2):
    def next_valid_index(s, i):
        backspaces = 0
        while i >= 0:
            if s[i] == '#':
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                return i
            i -= 1
        return -1

    i, j = len(s1) - 1, len(s2) - 1

    while i >= 0 or j >= 0:
        i = next_valid_index(s1, i)
        j = next_valid_index(s2, j)

        if i < 0 and j < 0:
            return True
        if i < 0 or j < 0 or s1[i] != s2[j]:
            return False

        i -= 1
        j -= 1

    return True

@pytest.mark.parametrize("s1, s2, expected", [
    ("abcde", "abcde", True),
    ("Uber Career Prep", "u#Uber Careee#r Prep", True),
    ("abcdef###xyz", "abcw#xyz", True),
    ("abcdef###xyz", "abcdefxyz###", False),
    ("xy#z", "xzz##z", True),
    ("x#y#z#", "a#", True),
    ("a#c", "b", False),
    ("#####", "", True),
    ("a###b", "b", True),
    ("a##b#c", "c", True)
])

def test_backspace_string_compare(s1, s2, expected):
    assert backspace_string_compare(s1, s2) == expected