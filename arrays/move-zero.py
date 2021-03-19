def move_zero(nums):
    for num in range(len(nums)):
        if nums[num] == 0:
            nums.append(nums[num])
            del nums[num]
    # if nums[-1] == 0:
    return nums

print(move_zero([0,1,0,3,12]))
print(move_zero([0,0,1]))

