"""
Question 6: MissingInteger
Given an integer n and a sorted array of integers of size n-1 which contains all
but one of the integers in the range 1-n, find the missing integer.

Time Complexity: O(log n), uses binary search
Space Complexity: O(1), no data structures

Technique:
Binary Search

Approach:
Since the array is sorted, we use binary search to find the missing number by
repeatedly narrowing down the search space based on the expected sequence of numbers.
If the middle element follows the correct order, the missing number is in the right half;
otherwise, it is in the left half. This process continues until the missing integer is identified.
"""

# Time: 28 min

import pytest

def find_missing_integer(arr, n):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1

    return left + 1

@pytest.mark.parametrize("arr, n, expected", [
    ([1, 2, 3, 4, 6, 7], 7, 5),
    ([1], 2, 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12, 9),
    ([2, 3, 4, 5], 5, 1),
    ([1, 2, 3, 4], 5, 5),
    ([1, 3, 4, 5, 6], 6, 2),
    ([1, 2, 3, 4, 5, 7], 7, 6),
    ([1, 2, 3, 5], 5, 4),
    ([1, 2], 3, 3),
    ([2], 3, 1),
])

def test_find_missing_integer(arr, n, expected):
    assert find_missing_integer(arr, n) == expected
