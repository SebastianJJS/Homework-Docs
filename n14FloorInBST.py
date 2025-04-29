"""
Question 14: FloorInBST
Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal
to the target) in the BST.

Time Complexity: O(h), at each step we move down one level of the tree; (O(log n) for balanced, O(n) for skewed trees.
Space Complexity: O(1), we only use a constant number of pointers

Technique:
Search binary search tree (BST)

Approach:
- Start at root.
- If current node’s value == target, return it.
- If current node’s value < target,  it’s a candidate; move right to find possibly closer floor.
- If current node’s value > target,  move left.
- Track best floor value found so far during traversal.
"""

# Time: 14 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def floorInBST(root, target):
    floor_val = None

    current = root
    while current:
        if current.data == target:
            return current.data
        elif current.data < target:
            floor_val = current.data  # Potential floor
            current = current.right
        else:
            current = current.left  # Current node too big, go left

    return floor_val

# Tests
def test_floor_exact_match_at_root():
    root = Node(8)
    root.left = Node(4)
    root.right = Node(10)
    assert floorInBST(root, 8) == 8

def test_floor_exact_match_on_subtree():
    root = Node(8)
    root.left = Node(4)
    root.right = Node(10)
    assert floorInBST(root, 10) == 10

def test_floor_smaller_target():
    root = Node(8)
    root.left = Node(4)
    root.right = Node(10)
    assert floorInBST(root, 9) == 8

def test_floor_no_floor():
    root = Node(5)
    root.left = Node(2)
    assert floorInBST(root, 1) == None

def test_floor_larger_than_all():
    root = Node(5)
    root.left = Node(2)
    root.right = Node(8)
    assert floorInBST(root, 20) == 8

def test_floor_on_subtree():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    assert floorInBST(root, 3) == 2

def test_empty_tree():
    assert floorInBST(None, 5) == None

def test_single_node():
    root = Node(7)
    assert floorInBST(root, 7) == 7
    assert floorInBST(root, 6) == None

def test_floor_with_negative_values():
    root = Node(0)
    root.left = Node(-5)
    root.left.left = Node(-10)
    assert floorInBST(root, -6) == -10