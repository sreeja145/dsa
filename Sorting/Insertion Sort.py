"""It is a simple sorting algorithm that works by the way you play cards in your hands.
The array is virtually split into sorted and unsorted parts."""


def Insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


A = [12, 13, 11, 3, 4, 15]
Insertion_Sort(A)
print(*A)

"""
Time Complexity: O(N^2)
Auxiliary Space: O(1)
"""
