""" Input : [1, 2, 3]
Output : [1], [1, 2], [2], [1, 2, 3], [2, 3], [3]

Input : [1, 2]
Output : [1], [1, 2], [2]"""

def subarrays(arr, start, end):
    if end == len(arr):
        return
    elif start > end:
        return subarrays(arr, 0, end + 1)
    else:
        print(arr[start:end + 1])
        return subarrays(arr, start + 1, end)


arr = [1, 2, 3]
subarrays(arr, 0, 0)

"""
Time Complexity: O(2^n)
Auxiliary Space: O(2^n)
"""