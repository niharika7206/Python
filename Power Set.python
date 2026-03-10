def subsets(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result

nums = [1,2,3]
print(subsets(nums))
