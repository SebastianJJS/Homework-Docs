"""
Question 2: Doubly Linked List (20 min max)
Implement basic doubly linked list operations.
Each function takes a Node object representing the head of the list.
Nodes store integer values, with both next and prev references.
Since Python uses references, node operations are done by adjusting '.next' and '.prev' directly.
No separate LinkedList class is used; all functions operate on the head Node.

Time Complexity:
- All insertions and deletions (insertAtFront, insertAtBack, insertAfter, insertBefore,
  deleteFront, deleteBack, deleteNode): O(1): direct reference updates without traversing the list.
- Length, reverseIterative, reverseRecursive: O(n): visit every node once

Space Complexity:
- O(1): only a constant number of variables are used.
"""

# Time: 24 min (reverseIterative and reverseRecursive, completed outside the 20 min limit)

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Insert at Front: O(1)
def insertAtFront(head, val):
    new_node = Node(val)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# Insert at Back: O(1) using tail
def insertAtBack(head, tail, val):
    new_node = Node(val)
    if not head:
        return new_node
    tail.next = new_node
    new_node.prev = tail
    return head

# Insert After loc Node: O(1)
def insertAfter(head, val, loc):
    if not loc:
        return head
    new_node = Node(val)
    new_node.next = loc.next
    new_node.prev = loc
    if loc.next:
        loc.next.prev = new_node
    loc.next = new_node
    return head

# Insert Before loc Node: O(1)
def insertBefore(head, val, loc):
    new_node = Node(val)
    new_node.next = loc
    if loc.prev:
        loc.prev.next = new_node
        new_node.prev = loc.prev
    else:
        head = new_node
    loc.prev = new_node
    return head

# Delete Front: O(1)
def deleteFront(head):
    if not head:
        return None
    if head.next:
        head.next.prev = None
    return head.next

# Delete Back: O(1) using tail
def deleteBack(head, tail):
    if not head or not tail:
        return None
    if tail.prev:
        tail.prev.next = None
    else:
        head = None  # Only one element
    return head

# Delete a Specific Node loc: O(1)
def deleteNode(head, loc):
    if not loc:
        return head
    if loc.prev:
        loc.prev.next = loc.next
    else:
        head = loc.next
    if loc.next:
        loc.next.prev = loc.prev
    return head

# Length of List: O(n)
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

# Reverse Iteratively: O(n)
def reverseIterative(head):
    if not head:
        return None
    current = head
    prev_node = None
    while current:
        next_node = current.next
        current.next = prev_node
        current.prev = next_node
        prev_node = current
        current = next_node
    return prev_node

# Reverse Recursively: O(n)
def reverseRecursive(head):
    def helper(curr):
        if not curr:
            return None
        curr.next, curr.prev = curr.prev, curr.next
        if curr.prev is None:
            return curr
        return helper(curr.prev)
    return helper(head)


# TESTING

# Helpers
def list_to_array(head):
    """Converts a doubly linked list to a list."""
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def array_to_doubly_list(arr):
    """Converts a Python list to a doubly linked list."""
    if not arr:
        return None, None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head, current

# Unit tests

def test_insertAtFront():
    head, tail = array_to_doubly_list([2, 3, 4])
    head = insertAtFront(head, 99)
    assert list_to_array(head) == [99, 2, 3, 4]

def test_insertAtBack():
    head, tail = array_to_doubly_list([1, 2, 3])
    head = insertAtBack(head, tail, 99)
    assert list_to_array(head) == [1, 2, 3, 99]

def test_insertAfter():
    head, tail = array_to_doubly_list([1, 2, 4])
    head = insertAfter(head, 99, head.next)  # Insert after node with value 2
    assert list_to_array(head) == [1, 2, 99, 4]

def test_insertBefore():
    head, tail = array_to_doubly_list([1, 3, 4])
    head = insertBefore(head, 99, head.next)  # Insert before node with value 3
    assert list_to_array(head) == [1, 99, 3, 4]

def test_deleteFront():
    head, tail = array_to_doubly_list([99, 2, 3])
    head = deleteFront(head)
    assert list_to_array(head) == [2, 3]

def test_deleteBack():
    head, tail = array_to_doubly_list([1, 2, 99])
    head = deleteBack(head, tail)
    assert list_to_array(head) == [1, 2]

def test_deleteNode():
    head, tail = array_to_doubly_list([1, 99, 3])
    head = deleteNode(head, head.next)  # Delete node with value 99
    assert list_to_array(head) == [1, 3]

def test_length():
    head, tail = array_to_doubly_list([1, 2, 3, 4])
    assert length(head) == 4
    head, tail = array_to_doubly_list([])
    assert length(head) == 0

def test_reverseIterative():
    head, tail = array_to_doubly_list([1, 2, 3])
    head = reverseIterative(head)
    assert list_to_array(head) == [3, 2, 1]

def test_reverseRecursive():
    head, tail = array_to_doubly_list([1, 2, 3])
    head = reverseRecursive(head)
    assert list_to_array(head) == [3, 2, 1]