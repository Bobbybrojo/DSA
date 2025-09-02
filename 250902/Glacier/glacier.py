from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# Add edges to starting points
edges = []
for r in range(n):
    edges.append((r, 0))
    edges.append((r, m - 1))
for c in range(m):
    edges.append((0, c))
    edges.append((n - 1, c))


# Returns whether or not the r, c point is in the grid
def in_range(r, c):
    return r >= 0 and c >= 0 and r < n and c < m


# Add any reachable zeros from the edges to the starting points
visited = set(edges)
q = deque(edges)
while q:
    r, c = q.popleft()

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 0:
            visited.add((nr, nc))
            q.append((nr, nc))

starting_points = list(visited)

# BFS melts glaciers and returns time at and the size of the final glacier melt
def bfs(points):
    visited = set(points)
    q = deque(list(map(lambda p: (p[0], p[1], 0), points)))

    max_time = 0
    latest_size = 0
    while q:
        r, c, time = q.popleft()

        if time > max_time:
            max_time = time
            latest_size = 0
        
        if time == max_time and grid[r][c] == 1:
            latest_size += 1

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                if grid[nr][nc] == 1:
                    q.append((nr, nc, time + 1))
                else:
                    q.append((nr, nc, time))

    return max_time, latest_size


time, size = bfs(starting_points)
print(f'{time} {size}')