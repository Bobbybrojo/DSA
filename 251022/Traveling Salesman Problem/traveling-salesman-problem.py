import sys

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# backtracking: O(nP(n,n))
def backtrack(curr):
    if len(curr) == n:
        curr.append(0)
        permutations.append(curr[:])
        curr.pop()
        return

    for i in range(0, n):
        if not visited[i]:
            visited[i] = True
            curr.append(i)
            backtrack(curr)
            visited[i] = False
            curr.pop()
    return

# Fill the permutations list with all orderings of visiting nodes
visited = [False] * n
visited[0] = True
permutations = []
backtrack([0])

# Calculate min cost from all permutations
min_sum = sys.maxsize
for perm in permutations:
    perm_sum = 0
    valid = True
    for i in range(1, len(perm)):
        grid_val = A[perm[i - 1]][perm[i]]

        if grid_val == 0:
            valid = False
        perm_sum += grid_val

        if not valid:
            break

    if not valid:
        continue

    if perm_sum < min_sum:
        min_sum = perm_sum
print(min_sum)