def triangular_sum(nums):
    if len(nums) == 1:
        return nums[0]
    while len(nums) > 1:
        new_nums = [0 for _ in range(len(nums) - 1)]
        for i in range(len(nums) - 1):
            new_nums[i] = (nums[i] + nums[i + 1]) % 10
        nums = new_nums
    return new_nums[0]
print(triangular_sum([1,2,3,4,5]))
print(triangular_sum([5]))