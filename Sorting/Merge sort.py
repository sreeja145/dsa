"""Merge sort algorithm works by dividing the array into smaller sub arrays
sortine them and merging the sorted subarrays together to form the final sorted array"""


def Merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        Merge_sort(L)
        Merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            arr[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1


arr = [12, 11, 13, 5, 6, 17, 0]
Merge_sort(arr)
print(*arr)

"""
Time Complexity: O(NlogN)
Space complexity:O(N)
"""
