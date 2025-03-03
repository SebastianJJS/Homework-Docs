"""
Question 3: ZeroSumSubArrays
Given an array of integers, count the number of subarrays that sum to zero.

Time Complexity: O(n), traverses the array once while maintaining prefix sums in a hashmap.
Space Complexity: O(n), for storing prefix sums in a hashmap.

Technique:
Hashing

Approach:
Track cumulative sums in a hashmap while iterating. If a sum repeats, the subarray between
occurrences sums to zero. Count zero-sum subarrays and update the hashmap with sum frequencies.
"""

# Time: 17 min

import pytest
from collections import defaultdict

def zero_sum_subarrays(arr):
    prefix_sum_counts = defaultdict(int)
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num

        if prefix_sum == 0:
            count += 1

        count += prefix_sum_counts[prefix_sum]

        prefix_sum_counts[prefix_sum] += 1

    return count

@pytest.mark.parametrize("arr, expected", [
    ([4, 5, 2, -1, -3, -3, 4, 6, -7], 2),
    ([1, 8, 7, 3, 11, 9], 0),
    ([8, -5, 0, -2, 3, -4], 2),
    ([0, 0, 0], 6),
    ([3, 4, -7, 1, 2, -6, 1, 2, 1], 5),
    ([1, -1, 2, -2, 3, -3], 6),
    ([1, 2, 3, 4, 5], 0),
    ([1, -1, 1, -1, 1, -1], 9),
    ([], 0),
    ([10, -10], 1)
])

def test_zero_sum_subarrays(arr, expected):
    assert zero_sum_subarrays(arr) == expected