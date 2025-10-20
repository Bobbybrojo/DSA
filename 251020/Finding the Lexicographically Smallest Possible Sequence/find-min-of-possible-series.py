n = int(input())

def backtrack(curr):
    global min_valid_seq

    if len(curr) == n:
        min_valid_seq = min(min_valid_seq, curr)
        return

    for i in range(4, 6 + 1):
        curr += str(i)

        is_invalid = False
        for l in range(2, len(curr) + 1, 2):
            hl = l//2
            if curr[-l:-hl] == curr[-hl:]:
                is_invalid = True
                break
        
        if not is_invalid:
            backtrack(curr)

        curr = curr[:-1]


min_valid_seq = "6" * n
backtrack("")
print(min_valid_seq)