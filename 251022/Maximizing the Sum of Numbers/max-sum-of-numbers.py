n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Brute force backtracking: O(P(n^2, n))
visited_rows = [False] * n

def backtracking(curr, cnt):
    if len(curr) == n:
        perms.append(curr[:])
        return

    for r in range(n):
        if not visited_rows[r]:
            visited_rows[r] = True
            curr.append(grid[r][cnt])
            
            backtracking(curr, cnt + 1)

            visited_rows[r] = False
            curr.pop()
    return

perms = []
backtracking([], 0)

max_sum = -1
for perm in perms:
    max_sum = max(max_sum, sum(perm))
print(max_sum)