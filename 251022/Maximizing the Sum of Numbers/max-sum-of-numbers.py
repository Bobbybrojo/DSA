n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Brute force backtracking
visited_rows = [False] * n
visited_cols = [False] * n

def backtracking(curr):
    global max_sum

    if len(curr) == n:
        max_sum = max(max_sum, sum(curr))
        return

    for r in range(n):
        for c in range(n):
            if not visited_rows[r] and not visited_cols[c]:
                visited_rows[r] = True
                visited_cols[c] = True
                curr.append(grid[r][c])
                
                backtracking(curr)

                visited_rows[r] = False
                visited_cols[c] = False
                curr.pop()
    return

max_sum = -1
backtracking([])
print(max_sum)