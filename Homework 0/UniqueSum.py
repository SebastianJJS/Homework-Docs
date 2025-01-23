"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
# def UniqueSum(arr):
#     total = 0
#     for num in set(arr):
#         total += num
#     return total
#
# print(UniqueSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
# print(UniqueSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))

"""
Time: 4 min
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def UniqueSuma(arr):
    seen = {}
    total = 0
    for n in arr:
        if n not in seen:
            total += n
            seen[n] = None
    return total

print(UniqueSuma([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(UniqueSuma([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))

"""
Time: 7 min
"""

# Sort and then compare i to i+1, Space Complex is O(1)

