""" It is the simplest sorting algorithm that works by swapping the adjacent elements if they were not in correct order.
Not suitable for large data sets as its average and worst case time complexity is quite high."""


def Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break


A = [45, 67, 23, 43, 21, 0, 11]
Bubble_sort(A)
print(*A)

"""
time complexity :O(N^2)
auxiliary space : O(1)
"""