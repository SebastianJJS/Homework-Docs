"""
Question 8: IsBST
Given a binary tree, determine if it is a binary search tree (BST).

Time Complexity: O(n), each node is visited once.
Space Complexity: O(h), call stack for recursion.

Technique:
Linked list/tree recursion

Approach:
Use recursion to check:
- The left subtree must only have nodes with values less than the current node.
- The right subtree must only have nodes with values greater than the current node.
Pass down valid value ranges (min, max) as we traverse.

Note: UCP doc allows assuming only int values, hence not tested for other input data types
"""
# 21 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root):
    def helper(node, min_val, max_val):
        if not node:
            return True
        if (min_val is not None and node.data <= min_val) or (max_val is not None and node.data >= max_val):
            return False
        return helper(node.left, min_val, node.data) and helper(node.right, node.data, max_val)
    return helper(root, None, None)

# Tests

def test_ucp_sample_1():
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)

    assert isBST(root) is True


def test_ucp_sample_2():
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(15)  # Violation here

    assert isBST(root) is False

def test_valid_bst_simple():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    assert isBST(root) is True

def test_invalid_bst_left_violation():
    root = Node(5)
    root.left = Node(6)  # Invalid, left child > parent
    root.right = Node(7)
    assert isBST(root) is False

def test_invalid_bst_right_violation():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(4)  # Invalid, right child < parent
    assert isBST(root) is False

def test_empty_tree():
    assert isBST(None) is True  # An empty tree is a valid BST

def test_single_node_tree():
    root = Node(10)
    assert isBST(root) is True

def test_valid_bst_large():
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right.left = Node(10)
    root.right.right = Node(14)
    assert isBST(root) is True

def test_invalid_bst_subtree():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(1)
    root.left.right = Node(12)  # Invalid: 12 > 10 but on left side
    assert isBST(root) is False

def test_invalid_bst_duplicates():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(5)  # Duplicate value
    assert isBST(root) is False

