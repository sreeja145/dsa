""" Given an array of integers arr[] of size N and an integer,
the task is to rotate the array elements to the left by d positions.
arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
Output: 3 4 5 6 7 1 2

Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
Output: 5 6 7 1 2 3 4
"""
# METHOD 1
"""def rotate(L,d,n):
    new=[]
    new=L[d+1:]+L[0:d+1]
    return new
arr=[1,2,3,4,5,6,7]
d=2
Length=len(arr)
final_Arr=rotate(arr,d-1,Length)
print(*final_Arr)
"""


# answer : 3 4 5 6 7 1 2

# Method 2

def rotate_one_by_one(arr, d, n):
    p = 1
    while p <= d:
        last = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = last
        p = p + 1


arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
Length = len(arr)
rotate_one_by_one(arr, d, Length)
print(*arr)
