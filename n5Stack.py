"""
Question 5: Stack (20 min max)
Implement a Stack class using a linked list.

Time Complexity:
- top, push, pop, isEmpty: O(1) time, direct pointer access, no traversal

Space Complexity:
- O(n): need space proportional to number of elements stored
"""

# Time: 12 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def top(self):
        if not self.top_node:
            return None
        return self.top_node.data

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if not self.top_node:
            return None
        val = self.top_node.data
        self.top_node = self.top_node.next
        return val

    def isEmpty(self):
        return self.top_node is None

# Tests

def test_isEmpty_initial():
    s = Stack()
    assert s.isEmpty() is True

def test_push_top():
    s = Stack()
    s.push(1)
    assert s.top() == 1
    s.push(2)
    assert s.top() == 2

def test_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    assert s.pop() == 3
    assert s.top() == 2
    assert s.pop() == 2
    assert s.top() == 1
    assert s.pop() == 1
    assert s.isEmpty() is True

def test_top_empty():
    s = Stack()
    assert s.top() is None

def test_pop_empty():
    s = Stack()
    assert s.pop() is None
