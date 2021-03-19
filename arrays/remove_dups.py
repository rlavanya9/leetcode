def removeDuplicates(nums):
    prev_num = 0
    count = 0
    srt_num = sorted(nums)
    for num in range(len(srt_num)):
        if nums[num] == prev_num:
            nums.append(nums[num])   
            del nums[num]  
        else:
            count += 1
        prev_num = nums[num]
    print(nums)
    return count

from typing import List

def removeDuplicates1(nums: List[int]) -> int:
    total_distinct_nums = 0
    prev_num = None
    for index in range(len(nums)):
      num = nums[index]
      if prev_num is None:
        prev_num = num
        total_distinct_nums += 1
        continue
      if num != prev_num:
        nums[total_distinct_nums] = num
        total_distinct_nums += 1
        prev_num = num
    print(nums)
    return total_distinct_nums

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates1([0,0,1,1,1,2,2,3,3,4]))