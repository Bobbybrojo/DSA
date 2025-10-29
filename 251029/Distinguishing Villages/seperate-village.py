n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# Tells if a r, c is in range of the grid
def in_range(r, c):
    return r >= 0 and c >= 0 and r < n and c < n

# DFS algorithm marks all neighbors visited as True in visited array
def dfs(r, c):
    count = 1
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if in_range(nr,nc) and grid[nr][nc] == 1:
            grid[nr][nc] = 0
            count += dfs(nr, nc)

    return count

count = 0
vil_counts = []
for r in range(n):
    for c in range(n):
        
        # If the current r, c is not visited mark it as visited and perform dfs
        if grid[r][c] == 1:
            grid[r][c] = 0
            vil_counts.append(dfs(r, c))
            count += 1

# Print results
vil_counts.sort()
print(count)
for vil in vil_counts:
    print(vil)
            