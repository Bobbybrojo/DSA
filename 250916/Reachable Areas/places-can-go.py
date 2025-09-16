from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(k)]
deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Mark starting points as seen
for pr, pc in points:
    grid[pr][pc] = 1

# Start with len(points) reachable cells
reachable_cells = len(points)

# Determine if we can perform BFS from the given cell
def can_go_to(r, c):
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    if grid[r][c] == 1:
        return False
    return True

# Perform bfs from all starting points
q = deque(points)
while q:
    r, c = q.popleft()

    for dr, dc in deltas:
        nr, nc = r + dr, c + dc

        if can_go_to(nr, nc):
            grid[nr][nc] = 1
            q.append((nr, nc))
            reachable_cells += 1

print(reachable_cells)