def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    number = str(x)
    i = 0
    j = len(number) - 1
    for i in range (len(number)):
        if i >= j:
            return True
        if number[i] == number[j]:
            j -= 1
            continue
        if number[i] != number[j]:
            break
    return False

        
print(isPalindrome(0))