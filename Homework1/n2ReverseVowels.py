"""
Question 2: ReverseVowels
Given a string, reverse the order of the vowels in the string.

Time Complexity: O(n) as each character was visited at most once.
Space Complexity O(n) because we require a mutable copy of the input.

Technique:
Opposite ends two pointer

Approach:
Convert the string to a list for mutability. Initialize two pointers
at the start and end. Move each pointer inward until both point to
vowels, then swap them. Repeat until the pointers meet, then return
the modified string.
"""

# Time: 7 min

import pytest

def reverse_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    str_list = list(string)
    left, right = 0, len(string) - 1

    while left < right:
        while left < right and str_list[right].lower() not in vowels:
            right -= 1
        while left < right and str_list[left].lower() not in vowels:
            left += 1

        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1
    return ''.join(str_list)

@pytest.mark.parametrize("string, expected", [
    ("Uber Career Prep", "eber Ceraer PrUp"),
    ("xyz", "xyz"),
    ("flamingo", "flominga"),
    ("aeiou", "uoiea"),
    ("AEIOU", "UOIEA"),
    ("a", "a"),
    ("b", "b"),
    ("Python", "Python"),
    ("A man, a plan, a canal, Panama", "a man, a plan, a canal, PanamA"),
    ("", ""),
])

def test_reverse_vowels(string, expected):
    assert reverse_vowels(string) == expected
