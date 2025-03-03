"""
Question 8: MergeIntervals
Given a list of integer pairs representing the low and high end of an interval,
inclusive, return a list in which overlapping intervals are merged.

Time Complexity: O(n log n), due to sorting the intervals. Merging is O(n).
Space Complexity: O(n), for storing the merged intervals.

Technique:
Sorting Algorithm + Forward/Backward Two-Pointer

Approach:
Sort the intervals by start time. Use one pointer to track the last merged interval
and another to iterate through the list. Merge overlapping intervals by extending the
end; otherwise, add a new interval. Repeat until all intervals are processed.
"""

# Time: 23 min

import pytest

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = []
    prev_start, prev_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= prev_end:
            prev_end = max(prev_end, end)
        else:
            merged.append((prev_start, prev_end))
            prev_start, prev_end = start, end

    merged.append((prev_start, prev_end))
    return merged

@pytest.mark.parametrize("intervals, expected", [
    ([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)], [(1, 3), (4, 8), (9, 12)]),
    ([(5, 8), (6, 10), (2, 4), (3, 6)], [(2, 10)]),
    ([(10, 12), (5, 6), (7, 9), (1, 3)], [(1, 3), (5, 6), (7, 9), (10, 12)]),
    ([], []),
    ([(1, 2)], [(1, 2)]),
    ([(1, 5), (2, 6), (8, 10), (9, 12)], [(1, 6), (8, 12)]),
    ([(1, 4), (5, 6), (7, 9)], [(1, 4), (5, 6), (7, 9)]),
    ([(1, 10), (2, 3), (4, 5), (6, 7), (8, 9)], [(1, 10)]),
    ([(2, 6), (1, 3), (7, 9), (10, 12)], [(1, 6), (7, 9), (10, 12)]),
    ([(1, 3), (2, 6), (8, 10), (15, 18)], [(1, 6), (8, 10), (15, 18)])
])

def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected

