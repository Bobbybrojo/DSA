from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def can_go(r: int, c: int) -> bool:
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    if grid[r][c] == 0 or grid[r][c] == -1:
        return False
    return True

q = deque()
def bfs(r, c):
    q.append((r, c))
    grid[r][c] = -1

    while q:
        r, c = q.popleft()
        grid[r][c] = -1

        for dr, dc in deltas:
            nr, nc = r + dr, c + dc

            if can_go(nr, nc):
                q.append((nr, nc))

bfs(0, 0)
print(1 if grid[n - 1][m - 1] == -1 else 0)
