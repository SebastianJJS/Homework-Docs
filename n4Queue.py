"""
Question 4: Queue (20 min max)
Implement a Queue class using a linked list.

Time Complexity:
- peek, enqueue, dequeue, isEmpty: O(1) time because we have references for the head and tail nodes

Space Complexity:
- O(n): need space proportional to number of elements stored
"""

# Time: 16 min

import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        if not self.head:
            return None
        return self.head.data

    # Add item to the back
    def enqueue(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Remove and return the first item
    def dequeue(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    # Check if the queue is empty
    def isEmpty(self):
        return self.head is None

# Tests

def test_isEmpty_initial():
    q = Queue()
    assert q.isEmpty() is True

def test_enqueue_peek():
    q = Queue()
    q.enqueue(1)
    assert q.peek() == 1
    q.enqueue(2)
    assert q.peek() == 1  # Peek should still see the first

def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    assert q.dequeue() == 1  # Remove 1
    assert q.peek() == 2     # Peek now sees 2
    assert q.dequeue() == 2  # Remove 2
    assert q.peek() == 3     # Peek now sees 3

def test_peek_empty():
    q = Queue()
    assert q.peek() is None

def test_dequeue_empty():
    q = Queue()
    assert q.dequeue() is None
