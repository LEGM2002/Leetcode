def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    s = ""
    strs.sort()
    first = strs[0]
    last = strs[len(strs) - 1]
    mix_len = min(len(first), len(last))
    i = 0
    for i in range(mix_len):
        if first[i] == last[i]:
            s += first[i]
        else:
            break
    return s
        
#print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))