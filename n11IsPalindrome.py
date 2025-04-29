"""
Question 11: IsPalindrome
Given a doubly linked list, determine if it is a palindrome

Time Complexity: O(n), we walk in from both ends once, each element visited once at most.
Space Complexity: O(1), only a pair of pointers.

Technique:
Doubly-linked-list forward/backward two-pointer

Approach:
Because we have both 'next' and 'prev' pointers, we can compare the first and last
nodes directly:
- Start left at the head and right at the tail.
- While left and right haven’t crossed, compare their data.
    If any mismatch occurs: not a palindrome.
- Move left forward and right backward each step (both pointers head towards the center).
- If every pair matches, the list is a palindrome.

Note: UCP doc allows assuming only int values, hence not tested for other input data types
"""

# Time spent: 16 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def isPalindrome(head: Node) -> bool:
    if head is None:
        return True

    # find tail
    tail = head
    while tail.next:
        tail = tail.next

    left, right = head, tail
    while left != right and left.prev != right:    # stop when pointers cross
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
    return True

# TESTING

# Helper
def array_to_dll(arr):
    """Convert an array into a doubly linked list; return head."""
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for val in arr[1:]:
        new = Node(val)
        cur.next = new
        new.prev = cur
        cur = new
    return head

# Tests
@pytest.mark.parametrize("arr, expected", [
    ([9, 2, 4, 2, 9], True),          # UCP Sample #1
    ([9, 12, 4, 2, 9], False),        # UCP Sample #2
    ([1, 2, 3, 2, 1], True),          # odd-length palindrome
    ([4, 5, 5, 4], True),             # even-length palindrome
    ([], True),                       # empty list is palindrome
    ([7], True),                      # single node is palindrome
    ([1, 2, 3], False),               # non-palindrome (odd-length)
    ([1, 2, 2, 3], False),            # non-palindrome (even-length)
    ([1, 2, 3, 4, 5, 4, 3, 2, 1], True),  # large palindrome
])

def test_isPalindrome(arr, expected):
    head = array_to_dll(arr)
    assert isPalindrome(head) is expected