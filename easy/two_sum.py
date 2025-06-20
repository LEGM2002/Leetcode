def two_sum(nums, target):
    hm = {}
    s = []
    i = 0
    for i in range(len(nums)):
        # hm has the number which if i sum
        # to the current the result is the target?
        if target - nums[i] in hm: 
            s.append(hm.get(target - nums[i]))
            s.append(i)
            break
        hm.update({nums[i] : i})
    return s

print(two_sum([2,7,11,15], 9))
#print(two_sum([3, 2, 4], 6))

