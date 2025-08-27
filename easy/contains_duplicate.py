def contains_duplicates(nums):
    """
    This works but in one case exceed the time limit,
    this because the length range is 1 to 100,000 and
    with a list the search time is O(n) because
    we iterate accross all list every time
    aux = []
    for num in nums:
        if num in aux:
            return True
        aux.append(num)
    return False """
    # Using a hashset which the search time is O(n)
    # hashset are implemented using hash tables
    # that's why the search time is constant
    aux = set()
    for num in nums:
        if num in aux:
            return True
        aux.add(num)
    return False

print(contains_duplicates([1,2,3,1]))