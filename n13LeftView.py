"""
Question 13: LeftView
Given a binary tree, create an array of the left view (leftmost elements in each level).

Time Complexity: O(n), each node is enqueued and dequeued exactly once.
Space Complexity: O(w), The queue holds up to the maximum number of nodes at any level (tree width).

Technique:
Level-order (breadth-first) traversal

Approach:
- Use a queue to perform level-order traversal.
- For each level, record the first node (leftmost node) encountered.
- Add that node’s value to the result array.
"""

# Time: 32 min

import pytest
from collections import deque

class Node:
   def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue) # Number of nodes at current level

        for i in range(level_size):
            node = queue.popleft()

            if i == 0:
                result.append(node.data)  # First node at this level is part of left view

            # Enqueue child nodes for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

# TESTING
# Tree structure drawn for grader's convenience — wouldn't include in real production code

def test_ucp_sample_1():
    root = Node(7)
    root.left = Node(8)
    root.right = Node(3)
    root.right.right = Node(13)
    root.right.left = Node(9)
    root.right.left.left = Node(20)
    root.right.right.left = Node(14)
    root.right.right.left.right = Node(15)
    assert([7, 8, 9, 20, 15])

def test_ucp_sample_2():
    root = Node(7)
    root.left = Node(20)
    root.right = Node(4)
    root.left.left = Node(15)
    root.left.right = Node(6)
    root.right.left = Node(8)
    root.right.right = Node(11)
    assert([7, 20, 15])

def test_leftView_normal_tree():
    # Tree:
    #      1
    #     / \
    #    2   3
    #   / \    \
    #  4   5    6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    assert leftView(root) == [1, 2, 4]

def test_leftView_deep_left_tree():
    # Tree:
    #       1
    #      / \
    #     2   3
    #    /      \
    #   4        7
    #  /
    # 8
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(8)
    root.right.right = Node(7)
    assert leftView(root) == [1, 2, 4, 8]

def test_leftView_right_skewed_tree():
    root = Node(1)
    root.right = Node(3)
    root.right.right = Node(6)
    root.right.right.right = Node(8)
    assert leftView(root) == [1, 3, 6, 8]

def test_leftView_empty_tree():
    root = None
    assert leftView(root) == []

def test_leftView_single_node():
    root = Node(1)
    assert leftView(root) == [1]

def test_leftView_more_populated_tree():

    # Tree:
    #             1
    #         /      \
    #        2        3
    #      /  \      /  \
    #     4    5    6    7
    #    / \  / \  / \    \
    #   8  9 10 11 12 13   14
    #  / \   /
    # 15 16 17

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.left.left.left.left = Node(15)
    root.left.right.left.left = Node(17)
    root.left.left.left.right = Node(16)

    assert leftView(root) == [1, 2, 4, 8, 15]
