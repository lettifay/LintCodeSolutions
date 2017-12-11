def mergeSortedArray(self, A, B):
    if A == None or B == None:
        return None
    
    result = []
    i,j=0,0
    while(i<len(A) and j<len(B)):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    
    if j < len(B):
        for k in range(j,len(B)):
            result.append(B[k])
    
    if i < len(A):
        for k in range(i,len(A)):
            result.append(A[k])
    
    return result