"""
Question 1: Singly Linked List (40 min max)
Implement basic singly linked list operations.
Each function takes a Node object representing the head of the list.
Nodes store integer values.
Since Python uses references, pointer operations are done by adjusting '.next' references directly.
No separate LinkedList class is used; all functions operate on the head Node.

Time Complexity:
- insertAtFront, insertAfter, deleteFront: O(1): direct reference updates without traversing the list.
- insertAtBack, insertBefore, deleteBack, deleteNode, length: O(n): must traverse up to n nodes to find the correct location.
- reverseIterative, reverseRecursive: O(n): visit every node once to reassign references.

Space Complexity:
- O(1): only a constant number of variables are used
"""

# Time: 38 min

import pytest
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Insert at Front: O(1)
def insertAtFront(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

# Insert at Back: O(n)
def insertAtBack(head, val):
    new_node = Node(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Insert After loc Node: O(1)
def insertAfter(head, val, loc):
    if not loc:
        return head
    new_node = Node(val)
    new_node.next = loc.next
    loc.next = new_node
    return head

# Insert Before loc Node: O(n)
def insertBefore(head, val, loc):
    new_node = Node(val)
    if head == loc:
        new_node.next = head
        return new_node
    current = head
    while current and current.next != loc:
        current = current.next
    if current:
        new_node.next = loc
        current.next = new_node
    return head

# Delete Front: O(1)
def deleteFront(head):
    if not head:
        return None
    return head.next

# Delete Back: O(n)
def deleteBack(head):
    if not head or not head.next:
        return None
    current = head
    while current.next and current.next.next:
        current = current.next
    current.next = None
    return head

# Delete a Specific Node loc: O(n)
def deleteNode(head, loc):
    if not head:
        return None
    if head == loc:
        return head.next
    current = head
    while current and current.next != loc:
        current = current.next
    if current and current.next == loc:
        current.next = loc.next
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
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Reverse Recursively: O(n)
def reverseRecursive(head):
    def helper(curr, prev):
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        return helper(next_node, curr)
    return helper(head, None)


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

# Unit tests

def test_insertAtFront():
    head = array_to_list([2, 3, 4])
    head = insertAtFront(head, 99)
    assert list_to_array(head) == [99, 2, 3, 4]

def test_insertAtBack():
    head = array_to_list([1, 2, 3])
    head = insertAtBack(head, 99)
    assert list_to_array(head) == [1, 2, 3, 99]

def test_insertAfter():
    head = array_to_list([1, 2, 4])
    head = insertAfter(head, 99, head.next)  # Insert after node with value 2
    assert list_to_array(head) == [1, 2, 99, 4]

def test_insertBefore():
    head = array_to_list([1, 3, 4])
    head = insertBefore(head, 99, head.next)  # Insert before node with value 3
    assert list_to_array(head) == [1, 99, 3, 4]

def test_deleteFront():
    head = array_to_list([99, 2, 3])
    head = deleteFront(head)
    assert list_to_array(head) == [2, 3]

def test_deleteBack():
    head = array_to_list([1, 2, 99])
    head = deleteBack(head)
    assert list_to_array(head) == [1, 2]

def test_deleteNode():
    head = array_to_list([1, 99, 3])
    head = deleteNode(head, head.next)  # Delete node with value 2
    assert list_to_array(head) == [1, 3]

def test_length():
    head = array_to_list([1, 2, 3, 4])
    assert length(head) == 4
    head = array_to_list([])
    assert length(head) == 0

def test_reverseIterative():
    head = array_to_list([1, 2, 3])
    head = reverseIterative(head)
    assert list_to_array(head) == [3, 2, 1]

def test_reverseRecursive():
    head = array_to_list([1, 2, 3])
    head = reverseRecursive(head)
    assert list_to_array(head) == [3, 2, 1]