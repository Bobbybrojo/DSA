from collections import deque

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

starting_points = []
for _ in range(k):
    ri, ci = map(int, input().split())
    starting_points.append((ri - 1, ci - 1))


# Returns whether the point is in the grid (0-indexed)
def in_range(r, c):
    return r >= 0 and c >= 0 and r < n and c < n

# Returns the number of cells that can be visited from the given starting points
def bfs(starting_points):
    
    visited = set(starting_points)
    q = deque(starting_points)

    while q:
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                q.append((nr, nc))

    return len(visited)

# Get the position of all stones on the grid
stones = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            stones.append((r, c))

# For all combinations of m stones removed, run bfs
def backtracking(count, last_idx):
    global max_reachable
    
    if count == m:
        reachable = bfs(starting_points)
        max_reachable = max(max_reachable, reachable)
        return

    for i in range(last_idx + 1, len(stones)):
        stone = stones[i]

        grid[stone[0]][stone[1]] = 0
        backtracking(count + 1, i)
        grid[stone[0]][stone[1]] = 1

max_reachable = 0
backtracking(0, -1)

print(max_reachable)