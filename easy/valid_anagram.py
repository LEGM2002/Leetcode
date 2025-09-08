def is_anagram(s, t):
    # length range from 1 to 50,000
    # anagram when two strings has the same letters
    # but in different order
    if len(s) != len(t):
        return False 
    return sorted(s) == sorted(t)

print(is_anagram("anagram", "nagaram"))