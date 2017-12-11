# 28. Search a 2D Matrix
def searchMatrix(matrix, target):
        if matrix == None or target == None:
            return False
        
        if len(matrix) == 0:
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        
        left,right = 0,(row*col - 1)
        while(left+1 < right):
            mid = (left+right)/2

            # get matrix index of mid point 
            x = mid/col
            y = mid%col
            
            if matrix[x][y] < target:
                left = mid
            else:
                right = mid
                
        x, y = left/col, left%col
        if matrix[x][y] == target:
            return True
        
        x, y = right/col, right%col
        if matrix[x][y] == target:
            return True
            
        return False