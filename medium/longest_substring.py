def longest_substring_without_repeating(s):
    # For solve this we need sliding window technique
    # for me is an extension of two pointer technique
    aux = set() # No repeated elements
    left = 0
    max_len = 0
    # left and right are the boundaries of the substring
    # if current char not in set we have a new char
    # else increment left until a new char
    for right in range(len(s)):
        while s[right] in aux:
            aux.remove(s[left])
            left += 1
        aux.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print(longest_substring_without_repeating("caabcdeaja"))