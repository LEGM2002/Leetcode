def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    # it works for exceed the memory on leetcode
    """ s = 0
    for i in range(0, x + 1):
        if i * i <= x:
            s = i
        else:
            break
    return s """
    # using binary search to reduce the searches
    if x == 0:
        return 0
    l = 1
    r = x
    while l <= r:
        mid = (l + r) // 2 # avoid decimals
        if mid * mid == x:
            return mid # best case
        elif mid * mid < x: # sqrt is on the right side
            l = mid + 1
        else: # sqrt is on the left side
            r = mid - 1
    return r

print(mySqrt(2147395599))
        