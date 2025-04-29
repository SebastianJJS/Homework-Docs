"""
Question 6: Deque (20 min max)
Implement a Deque class using a doubly linked list.

Time Complexity:
- front, back, pushBack, pushFront, popFront, popBack, isEmpty: O(1) time, direct pointer access, no traversal

Space Complexity:
- O(n): need space proportional to number of elements stored
"""

# Time: 19 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        if not self.head:
            return None
        return self.head.data

    def back(self):
        if not self.tail:
            return None
        return self.tail.data

    def pushBack(self, x):
        new_node = Node(x)
        if not self.tail:
            # If empty, both head and tail are the new node
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pushFront(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def popFront(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head:
            # Update new head's prev to None
            self.head.prev = None
        else:
            # If deque became empty, reset tail too
            self.tail = None
        return val

    def popBack(self):
        if not self.tail:
            return None
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            # Update new tail's next to None
            self.tail.next = None
        else:
            # If deque became empty, reset head too
            self.head = None
        return val

    def isEmpty(self):
        return self.head is None


# Tests

def test_isEmpty_initial():
    d = Deque()
    assert d.isEmpty() is True

def test_pushBack_and_back():
    d = Deque()
    d.pushBack(10)
    assert d.back() == 10
    d.pushBack(20)
    assert d.back() == 20

def test_pushFront_and_front():
    d = Deque()
    d.pushFront(10)
    assert d.front() == 10
    d.pushFront(20)
    assert d.front() == 20

def test_pushFront_pushBack_combination():
    d = Deque()
    d.pushFront(2)
    d.pushBack(3)
    d.pushFront(1)
    assert d.front() == 1
    assert d.back() == 3

def test_popFront():
    d = Deque()
    d.pushBack(1)
    d.pushBack(2)
    d.pushBack(3)

    assert d.popFront() == 1
    assert d.front() == 2
    assert d.popFront() == 2
    assert d.front() == 3
    assert d.popFront() == 3
    assert d.isEmpty() is True

def test_popBack():
    d = Deque()
    d.pushFront(1)
    d.pushFront(2)
    d.pushFront(3)

    assert d.popBack() == 1
    assert d.back() == 2
    assert d.popBack() == 2
    assert d.back() == 3
    assert d.popBack() == 3
    assert d.isEmpty() is True

def test_front_and_back_empty():
    d = Deque()
    assert d.front() is None
    assert d.back() is None

def test_popFront_popBack_empty():
    d = Deque()
    assert d.popFront() is None
    assert d.popBack() is None