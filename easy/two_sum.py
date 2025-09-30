def two_sum(nums, target):
    hm = {}
    s = []
    i = 0
    for i in range(len(nums)):
        # does hm have the number which if i adding
        # to the current the result is the target?
        if target - nums[i] in hm: # if needed value is in hm
            # append to s the value on hm using the key
            s.append(hm.get(target - nums[i])) 
            # append to s the current index
            s.append(i)
            break
        # if not append to hm the value as key and i as value
        hm.update({nums[i] : i})
    return s

print(two_sum([2,7,11,15], 9))
#print(two_sum([3, 2, 4], 6))

