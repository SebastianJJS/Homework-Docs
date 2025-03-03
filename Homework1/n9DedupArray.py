"""
Question 9: DedupArray
Given a sorted array of non-negative integers, modify the array by removing duplicates so each element
only appears once. If arrays are static (aka, not dynamic/resizable) in your language of choice, the
remaining elements should appear in the left-hand side of the array and the extra space in the right-hand
side should be padded with -1s.

Time Complexity: O(n), traverses the array once with a two-pointer approach.
Space Complexity: O(1), modifies the array in place without using extra space.

Technique:
Forward Two-Pointer Technique

Approach:
Use two pointers: one (write) to track unique elements and another (read) to iterate through the array.
Place unique elements at write and increment both pointers.
"""
# Time: 9 min

import pytest

def dedup_array(arr):
    if not arr:
        return []

    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1

    return arr[:write]

@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], [1, 2, 3, 4]),
    ([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15], [0, 1, 4, 5, 8, 9, 10, 11, 15]),
    ([1, 3, 4, 8, 10, 12], [1, 3, 4, 8, 10, 12]),
    ([1, 1, 1, 1, 1], [1]),
    ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
    ([5, 5, 5, 5, 5, 5, 5], [5]),
    ([1, 2, 3, 4, 5, 5, 5, 5], [1, 2, 3, 4, 5]),
    ([7, 8, 9, 10, 10, 10, 10, 10], [7, 8, 9, 10]),
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
    ([], []),
])

def test_dedup_array(arr, expected):
    assert dedup_array(arr) == expected