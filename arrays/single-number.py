def singleNumber(nums):
    ret = 0
    for num in nums:
        ret ^= num
    return ret