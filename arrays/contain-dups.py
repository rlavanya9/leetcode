# def containsDuplicate(nums):
#     sort_nums = sorted(nums)
#     for i in range(len(sort_nums)):
#         for j in range(i):
#             if sort_nums[i] == sort_nums[j]:
#                 return True
#     return False

def containsDuplicate(nums):
    sort_nums = sorted(nums)
    for i in range(len(sort_nums)-1):
        if sort_nums[i + 1] == sort_nums[i]:
            return True
    return False

# def containsDuplicate(nums):
#     sort_nums = sorted(nums)
#     for i in range(len(sort_nums)):
#         if nums[i + 1] == nums[i]:
#             return True
#     return False


    
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(containsDuplicate([0]))