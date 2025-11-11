from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Returns true if the r, c pair is in the grid
def in_range(r, c):
    return r >= 0 and c >= 0 and r < n and c < m

# Traverse through all water nodes surrounding glaciers
def bfs(start):
    

    q = deque([start])
    while q:
        r, c, depth = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                q.append((nr, nc, depth + 1))

# Melts glaciers touching an outside water
def melt():
    global last_melt_cnt

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                touching_outside_water = False
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if in_range(nr, nc) and visited[nr][nc]:
                        touching_outside_water = True
                        break

                if touching_outside_water:
                    grid[r][c] = 0
                    last_melt_cnt += 1

# True if a glacier still exists on the grid, False otherwise
def glacier_exists():
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                return True

    return False

elapsed_time = 0
last_melt_cnt = 0
while glacier_exists():
    # Track time and melt count
    elapsed_time += 1
    last_melt_cnt = 0

    # Fill visited with True if it is a water not surrounded by glaciers (outside water)
    visited = [[False] * m for _ in range(n)]
    bfs((0, 0, 0))

    # Turn glaciers into water if they are touching an outside water
    melt()

print(elapsed_time, last_melt_cnt)


