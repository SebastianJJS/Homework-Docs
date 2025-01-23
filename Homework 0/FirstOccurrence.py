"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

def FirstOccurrence(str):
    occurrence_count = {}
    result = ""
    for c in str:
        if c not in occurrence_count:
            result += c
            occurrence_count[c] = 1
    return result

"""
Time: 5 min
"""