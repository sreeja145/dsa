def reverseList(A,start,end):
    while start<end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
A=[3,4,56,78,0,1]
length=len(A)
reverseList(A,0,length-1)
print(*A)