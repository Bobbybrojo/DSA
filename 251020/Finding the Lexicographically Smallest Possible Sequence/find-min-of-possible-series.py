n = int(input())

# Backtracking algorithm
def backtrack(curr):

    # Return the first sequence we find (the smallest one)
    if len(curr) == n:
        return curr

    for i in range(4, 6 + 1):
        curr += str(i)

        # Check if sequence is valid
        is_invalid = False
        for l in range(2, len(curr) + 1, 2):
            hl = l//2
            if curr[-l:-hl] == curr[-hl:]:
                is_invalid = True
                break
        
        # If valid backtrack
        if not is_invalid:
            result = backtrack(curr)
            if result:
                return result

        curr = curr[:-1]

    # Return None if no valid sequences
    return None


result = backtrack("")
print(result if result else "6" * n)