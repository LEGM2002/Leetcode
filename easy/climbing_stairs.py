def climbing_stairs(n, memo={}):
    # After an analysis i discovered that 
    # the pattern is the fibonacci sequence
    # with 1's we have n
    # with one 2 and then 1's we have n - 1
    # with two 2 and then 1's we have n - 2
    # ways(n) = ways(n - 1) + ways(n - 2)
    # THIS WORKS BUT EXCEDEED TIME LIMIT, USE MEMOIZATION
    """ if n <= 1 : # f(0) or f(1) = 1
        return 1
    # f(n) = f(n - 1) + f(n - 2)
    return climbing_stairs(n - 1) + climbing_stairs(n - 2) """
    if n in memo: # Verify if n was compute previously
        return memo[n]
    if n <= 1: # Base case
        return 1
    memo[n] = climbing_stairs(n - 1, memo) + climbing_stairs(n - 2, memo) # Add value no compute previously
    return memo[n]

print(climbing_stairs(5))
"""
    climbing_stairs(5)
    ├── climbing_stairs(4)
    │   ├── climbing_stairs(3)
    │   │   ├── climbing_stairs(2)
    │   │   │   ├── climbing_stairs(1) → 1
    │   │   │   └── climbing_stairs(0) → 1
    │   │   └── climbing_stairs(1) → 1
    │   └── climbing_stairs(2)
    │       ├── climbing_stairs(1) → 1
    │       └── climbing_stairs(0) → 1
    └── climbing_stairs(3)
        ├── climbing_stairs(2)
        │   ├── climbing_stairs(1) → 1
        │   └── climbing_stairs(0) → 1
        └── climbing_stairs(1) → 1
    """