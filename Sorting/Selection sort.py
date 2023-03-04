""" It is a simple and efficient algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the array and
moving it to the sorted portion of the array or list of elements."""
A=[64,32,43,22,23,11]
for i in range(len(A)):
    min_idx=i
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx=j
    A[min_idx],A[i]=A[i],A[min_idx]
print(*A)
"""
Time Complexity:O(N^2)
Auxiliary Space:O(1)

"""