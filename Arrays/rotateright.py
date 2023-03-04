""" """
def Right_rotate(Arr, n, d):
    d = d % n
    for i in range(0, n):
        if i < d:
            print(Arr[n + i - d], end=" ")
        else:
            print(Arr[i - d], end=" ")


Array = [1, 2, 3, 4, 5]
N = len(Array)
K = 2
Right_rotate(Array, N, K)

# answer: 4 5 1 2 3