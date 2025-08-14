def letter_case_permutation(s):
    # Change consonant or vowel into upper or lower
    # get all permutations
    result = []

    def backtrack(index, new_string):
        # iterate over all characters
        if index == len(s):
            result.append(new_string)
            return

        char = s[index]
        if char.isalpha():  # if it’s a letter, branch into lower/upper
            backtrack(index + 1, new_string + char.lower())
            backtrack(index + 1, new_string + char.upper())
        else:  # if it’s a number append it and continue
            backtrack(index + 1, new_string + char)

    backtrack(0, "")
    return result

print(letter_case_permutation("a1b2"))