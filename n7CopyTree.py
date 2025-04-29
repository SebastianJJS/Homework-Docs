"""
Question 7: CopyTree
Given a binary tree, create a deep copy. Return the root of the new tree.

Time Complexity: O(n), we visit each node once.
Space Complexity: O(h) call stack for recursion.

Technique:
Linked list/tree recursion

Approach:
Recursively create a new node for each existing node,
copying the value, and recursively linking its left and right subtrees.
"""

# Time: 24 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root):
    if not root:
        return None
    new_node = Node(root.data)
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)
    return new_node

# TESTING

# Helper
def trees_are_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    return trees_are_identical(root1.left, root2.left) and trees_are_identical(root1.right, root2.right)


# Tests

def test_copy_single_node():
    root = Node(1)
    copied = copyTree(root)
    assert trees_are_identical(root, copied)
    assert root is not copied

def test_copy_full_two_levels():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    copied = copyTree(root)
    assert trees_are_identical(root, copied)
    assert root is not copied

def test_copy_left_skewed():
    root = Node(5)
    root.left = Node(4)
    root.left.left = Node(3)
    root.left.left.left = Node(2)
    copied = copyTree(root)
    assert trees_are_identical(root, copied)
    assert root is not copied

def test_copy_right_skewed():
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    copied = copyTree(root)
    assert trees_are_identical(root, copied)
    assert root is not copied

def test_copy_empty_tree():
    root = None
    copied = copyTree(root)
    assert copied is None

def test_copy_unbalanced_tree():
    root = Node(10)
    root.left = Node(5)
    root.left.right = Node(7)
    root.right = Node(15)
    copied = copyTree(root)
    assert trees_are_identical(root, copied)
    assert root is not copied