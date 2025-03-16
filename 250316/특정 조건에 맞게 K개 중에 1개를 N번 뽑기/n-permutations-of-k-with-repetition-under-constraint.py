K, N = map(int, input().split())

# backtracking approach
def backtrack(curr, idx):

    # When lenth of current array is N, print current array and newline
    if len(curr) == N:
        for l in curr:
            print(f'{l}', end=' ')
        print()
        return

    # Select a number from 1 - K (inclusive)
    for i in range(1, K + 1):
        # If last 2 numbers are same as selected number: skip
        if idx >= 2 and  curr[idx - 1] == curr[idx - 2] and curr[idx - 2] == i:
            continue

        # add selected number to curr
        curr.append(i)

        # recurse
        backtrack(curr, idx + 1)

        # backtrack
        curr.pop()

backtrack([], 0)
