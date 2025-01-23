"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def ZeroSum(arr):
    number_counts = {}
    total_pairs = 0

    for number in arr:
        complement = -number
        if number_counts.get(complement, 0) > 0:
            total_pairs += 1
            number_counts[complement] -= 1
            # print(number_counts)
        else:
            number_counts[number] = number_counts.get(number, 0) + 1
            # print(number_counts)
    return total_pairs

"""
Time: 28 min
Follow-Up: Not completed
"""
