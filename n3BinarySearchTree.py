"""
Question 3: Binary Search Tree (40 min max)
Implement basic Binary Search Tree operations.
Each Node has integer data, and left and right references.

Time Complexity:
- min, max, contains, insert, delete: O(log n) for balanced trees (but O(n) if unbalanced)

Space Complexity:
- O(1) for iterative methods; O(h) call stack for recursion
"""

# Time: 40 min, delete method not completed

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def contains(self, val):
        current = self.root
        while current:
            if val == current.data:
                return True
            elif val < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return

        current = self.root
        while True:
            if val == current.data: # No duplicates allowed
                return
            elif val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    return

    def delete(self, val):
        def delete_rec(node, val):
            if not node:
                return None

            if val < node.data:
                node.left = delete_rec(node.left, val)
            elif val > node.data:
                node.right = delete_rec(node.right, val)
            else:
                # Case 3: Two children
                # TODO: Replace node with the smallest in the right subtree
                pass

            return node

        self.root = delete_rec(self.root, val)

# TESTING

# Helper

def array_to_bst(arr):
    bst = BinarySearchTree()
    for val in arr:
        bst.insert(val)
    return bst

# Tests

def test_min():
    bst = array_to_bst([8, 3, 10, 1, 6])
    assert bst.min() == 1
    empty_bst = BinarySearchTree()
    assert empty_bst.min() is None

def test_max():
    bst = array_to_bst([8, 3, 10, 1, 6, 14])
    assert bst.max() == 14
    empty_bst = BinarySearchTree()
    assert empty_bst.max() is None

def test_contains():
    bst = array_to_bst([8, 3, 10, 1, 6])
    assert bst.contains(6) is True
    assert bst.contains(5) is False
    empty_bst = BinarySearchTree()
    assert empty_bst.contains(10) is False

def test_insert():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(5)  # Duplicate, should do nothing
    assert bst.contains(5) is True
    assert bst.contains(3) is True
    assert bst.contains(7) is True
    assert bst.contains(10) is False

def test_delete():  # Fails due to uncomplete function
    bst = array_to_bst([8, 3, 10, 1, 6])
    bst.delete(1)
    assert bst.contains(1) is False

