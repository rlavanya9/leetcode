def rotate_matrix(nums,k): 
    for idx in range(k):
        last_val = nums[-1]
        # print(idx)
        print(last_val)
        for j in range(len(nums)-1,-1,-1):
            nums[j] = nums[j-1]
        nums[0] = last_val
    return nums

print(rotate_matrix([1,2,3,4,5,6,7],3))
print(rotate_matrix([-1,-100,3,99],2))