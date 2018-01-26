# 41. Maximum Subarray
def maxSubArray(nums):
    result = -65535
    cur_sum = 0
    for num in nums:
        cur_sum = max(cur_sum + num, num)
        result = max(result,cur_sum)
    return result