"""
Question 9: DedupSortedList
Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

Time Complexity: O(n), we traverse the list once.
Space Complexity: O(1), only a constant number of variables are used

Technique:
Linked list one-pass traversal

Approach:
Since the list is sorted, duplicates are adjacent.
We traverse the list with a single pointer:
- If current node's value equals next node's value, skip the next node.
- Otherwise, move to next.

Note: UCP doc allows assuming only int values, hence not tested for other input data types
"""

# Time: 9 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def dedupSortedList(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            # Skip duplicate node
            current.next = current.next.next
        else:
            current = current.next
    return head

# TESTING

# Helpers
def list_to_array(head):
    """Converts a linked list to an array."""
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def array_to_list(arr):
    """Converts an array to a linked list."""
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Tests
@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 2, 4, 5, 5, 5, 10, 10], [1, 2, 4, 5, 10]),  # UCP Sample #1
    ([8,8,8,8], [8]),                    # UCP Sample #2 / All nodes are the same
    ([1, 1, 2, 3, 3], [1, 2, 3]),        # Regular case with duplicates
    ([1, 2, 3], [1, 2, 3]),              # No duplicates
    ([], []),                            # Empty list
    ([1], [1]),                          # Single element
    ([1, 1, 2, 2, 3, 3, 4, 4], [1, 2, 3, 4]),  # Many duplicates
    ([1, 2, 2, 2, 3], [1, 2, 3]),         # Clustered duplicates
    ([1, 2, 3, 4, 4, 4, 4, 5], [1, 2, 3, 4, 5]), # Duplicates clustered before final node
])

def test_dedupSortedList(arr, expected):
    head = array_to_list(arr)
    dedupSortedList(head)
    assert list_to_array(head) == expected