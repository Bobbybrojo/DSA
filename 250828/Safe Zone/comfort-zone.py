import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

'''
Subtract the grid by 1 for each k
Find number of connected components with vals > 0
'''

# Sink the grid by one
def sink_grid():
    for r in range(n):
        for c in range(m):
            grid[r][c] -= 1

# Find the max k value that == max value in grid - 1
max_k = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] > max_k:
            max_k = grid[r][c]

# Determines if we can run dfs on this position
def can_go(r: int, c: int) -> bool:
    if r < 0 or r >= n or c < 0 or c >= m:
        return False
    if grid[r][c] <= 0 or visited[r][c]:
        return False
    return True

dfs_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# Use dfs to find all the connected components on the grid
def dfs(r: int, c: int):
    visited[r][c] = True

    for dr, dc in dfs_deltas:
        nr, nc = r + dr, c + dc
        if can_go(nr, nc):
            dfs(nr, nc)

answer = (1, 0)
# Find number of connected components not submerged for each k
for k in range(1, max_k):
    sink_grid()

    safe_zones = 0
    visited = [[False] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if grid[r][c] <= 0:
                visited[r][c] = True
            elif not visited[r][c]:
                dfs(r, c)
                safe_zones += 1

    if safe_zones > answer[1]:
        answer = (k, safe_zones)

print(f'{answer[0]} {answer[1]}')