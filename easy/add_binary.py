def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        # mod because of 1 + 1 = 10 -> carry = 2
        s.append(str(carry % 2))
        # if i have carry 0 -> 0 
        # if i have carry 1 ->  0
        # if i have carry 2 -> 1
        # carry is 1 only when the sum is 2 (1 + 1)
        carry //= 2  
    if carry == 1:
        s.append("1")
    return "".join(reversed(s))

print(addBinary("0", "0"))