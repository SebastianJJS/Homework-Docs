"""
Question 12: DisconnectCycle
Given a singly linked list, disconnect the cycle, if one exists.

Time Complexity: O(n), two sequential passes over the list (no nested traversal).
Space Complexity: O(1), only a few pointers used.

Technique:
Linked list fast-slow two-pointer

Approach:
- Use slow and fast pointers to detect if a cycle exists.
- Once detected, reset one pointer to head, and move both pointers one step at a time.
- When they meet, the node before slow needs its '.next' set to None to break the cycle.
"""

# Time: 40+ min
# My initial implementation (28 min) worked for all regular cases.
# I spent extra time handling the edge case where the cycle started at the head.

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def disconnectCycle(head):
    if not head:
        return head

    slow = head
    fast = head

    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No cycle
        return head

    # Find start of cycle
    slow = head
    if slow == fast:
        # Cycle starts at head
        while fast.next != slow:
            fast = fast.next
        fast.next = None
    else:
        # Cycle starts later
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

    return head

# TESTING

# Helpers
def list_to_cycle(arr, position):
    """Creates a linked list from arr and creates a cycle at index 'position'."""
    if not arr:
        return None
    head = Node(arr[0])
    nodes = [head]
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        nodes.append(new_node)
        current.next = new_node
        current = new_node
    if position != -1 and 0 <= position < len(nodes):
        current.next = nodes[position]
    return head

def list_to_array(head, limit=100):
    """Convert linked list to array; limit steps to avoid infinite loops."""
    result = []
    count = 0
    while head and count < limit:
        result.append(head.data)
        head = head.next
        count += 1
    return result

# Tests
@pytest.mark.parametrize("arr, pos, expected", [
    ([10, 18, 12, 9, 11, 4], 2, [10, 18, 12, 9, 11, 4]),   # cd
    ([10, 18, 12, 9, 11, 4], 5, [10, 18, 12, 9, 11, 4]),   # UCP Sample #2 / cycle at tail
    ([3, 2, 0, -4], 1, [3, 2, 0, -4]),              # Cycle in the middle
    ([1, 2], 0, [1, 2]),                            # Cycle at head
    ([1], 0, [1]),                                  # Single node, self-cycle
    ([1], 0, [1]),                                  # Single node, no cycle
    ([], 0, []),                                    # Empty list
    ([1, 2], 7, [1, 2]),                            # Invalid cycle position
    ([1, 2, 3, 4, 5], -1, [1, 2, 3, 4, 5]),         # Normal list, no cycle
    (list(range(1, 101)), 1, list(range(1, 101))),  # Large list cycle
])
def test_disconnectCycle(arr, pos, expected):
    head = list_to_cycle(arr, pos)
    head = disconnectCycle(head)
    assert list_to_array(head) == expected