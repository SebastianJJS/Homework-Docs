"""
Question 1: MaxMeanSubArray
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

Time Complexity: O(n) because the array is traversed once with a sliding window.
Space Complexity: O(1) because the function operates in place, using only a few integer variables.

Technique:
A fixed sliding window with length k

Approach:
We use a fixed-size sliding window, first computing the sum of the
initial k elements. As the window moves, we update the sum by adding
the new element and removing the leftmost one, tracking the maximum sum.
The result is the highest sum divided by k.
"""

# Time: 22 min

import pytest
def max_mean_subarray(arr, k):
    if not isinstance(k, int) or k <= 0:
        return None

    if len(arr) < k:
        return None


    left = 0
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[left]
        left += 1
        max_sum = max(max_sum, window_sum)

    return max_sum / k

@pytest.mark.parametrize("array, k, expected", [
    ([4, 5, -3, 2, 6, 1], 2, 4.5),
    ([4, 5, -3, 2, 6, 1], 3, 3.0),
    ([1, 1, 1, 1, -1, -1, 2, -1, -1], 3, 1.0),
    ([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5, 1.0),
    ([], 5, None),
    ([1], 5, None),
    ([1, 2], 1, 2.0),
    ([-1, -2, -3, -4, -5], 2, -1.5),
    ([0, 0, 0, 0, 0], 2, 0.0),
    ([10, 20, 30, 40, 50], None, None),
])

def test_max_mean_subarray(array, k, expected):
    assert max_mean_subarray(array, k) == expected