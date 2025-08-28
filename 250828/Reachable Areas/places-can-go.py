from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(k)]
deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def can_go(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False
    if grid[r][c] == 1:
        return False
    return True

def bfs(sr, sc):
    cells_reached = 0

    q = deque()
    q.append((sr, sc))
    grid[sr][sc] = 1
    cells_reached += 1

    while q:
        r, c = q.popleft()

        for dr, dc in deltas:
            nr, nc = r + dr, c + dc

            if can_go(nr, nc):
                grid[nr][nc] = 1
                cells_reached += 1
                q.append((nr, nc))

    return cells_reached

reachable_cells = 0
for r, c in points:
    if can_go(r, c):
        reachable_cells += bfs(r, c)

print(reachable_cells)