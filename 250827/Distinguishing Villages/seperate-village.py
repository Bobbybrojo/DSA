n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Find connected components
# using DFS starting at every valid position
# never unmark from visited array
# - can modify visited array directly on grid (maybe)

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

deltas = [
    (1, 0),  # down
    (0, 1),  # right
    (-1, 0), # up
    (0, -1), # left
]

def can_go(r, c):
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    if visited[r][c] or grid[r][c] == 0:
        return False
    return True

connected_component_sizes = []
def dfs(r, c):
    size = 1
    for dr, dc in deltas:
        nr, nc = r + dr, c + dc

        if can_go(nr, nc):
            visited[nr][nc] = True
            size += dfs(nr, nc)

    return size

for r in range(n):
    for c in range(n):
        if not visited[r][c] and grid[r][c] == 1:
            visited[r][c] = True
            connected_component_sizes.append(dfs(r, c))

            
print(len(connected_component_sizes))
for size in sorted(connected_component_sizes):
    print(size)
