#  463. Sort Integers
def sortArray(A):
    for i in range(len(A)):
        for j in range(len(A[i:])):
            if A[i] > A[i+j]:
                A[i],A[i+j] = A[i+j],A[i]
    return A