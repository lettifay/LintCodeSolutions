# 39. Recover Rotated Sorted Array
def recoverRotatedSortedArray(nums):
    if nums == None:
        return None
    if len(nums) == 1:
        return nums

    for n in range(1,len(nums)):
        if nums[n] < nums[0]:
            nums[-n:],nums[:(len(nums)-n)] = nums[:n],nums[n:]
            break
    return nums