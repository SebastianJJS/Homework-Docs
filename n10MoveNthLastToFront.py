"""
Question 10: MoveNthLastToFront
Given a singly linked list, move the nth from the last element to the front of the list.

Time Complexity: O(n), we traverse the list once.
Space Complexity: O(1), only a constant number of variables are used.

Technique:
Linked list fast-slow two-pointer

Approach:
Use two pointers:
- Move the fast pointer n steps ahead.
- Then move slow and fast together until fast reaches the end.
- Slow pointer will be just before the node to move.
- Rearrange pointers to move the node to the front.

Note: UCP doc allows assuming only int values, hence not tested for other input data types
"""
# Time: 36 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def moveNthLastToFront(head, n):
    if not head or n <= 0:
        return head

    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    # Move fast pointer n steps ahead
    for _ in range(n):
        if not fast.next:
            return head
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # slow.next is the node we want to move
    node_to_move = slow.next
    if node_to_move == head:
        return head  # Already at front

    slow.next = node_to_move.next  # Remove node_to_move from current position
    node_to_move.next = head       # Insert node_to_move at the front
    return node_to_move

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
@pytest.mark.parametrize("arr, n, expected", [
    ([15, 2, 8, 7, 20, 9, 11, 6, 19], 2, [6, 15, 2, 8, 7, 20, 9, 11, 19]),  # UCP Sample #1
    ([15, 2, 8, 7, 20, 9, 11, 6, 19], 7, [8, 15, 2, 7, 20, 9, 11, 6, 19]),  # UCP Sample #2
    ([1, 2, 3], 1, [3, 1, 2]),    # Move last node
    ([1, 2, 3], 3, [1, 2, 3]),    # Move first node (no change)
    ([5], 1, [5]),                # Single node
    ([], 1, []),                  # Empty list
    ([1, 2], 5, [1, 2]),          # k > length (no change)
    ([1, 2, 3], 0, [1, 2, 3]),    # k = 0 (invalid)
    ([4, 5, 6], -1, [4, 5, 6]),   # negative k (invalid)
])

def test_moveNthLastToFront(arr, n, expected):
    head = array_to_list(arr)
    new_head = moveNthLastToFront(head, n)
    assert list_to_array(new_head) == expected