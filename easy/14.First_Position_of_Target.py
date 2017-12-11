# 14. First Position of Target, use binary search.
def binarySearch(nums, target):
    if nums == None or target == None:
        return -1
    
    left,right = 0, len(nums)-1
    while(left+1 < right):
        mid = (left+right)/2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    else:
        return -1