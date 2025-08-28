from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def can_go(r: int, c: int) -> bool:
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    if visited[r][c] or grid[r][c] == 0:
        return False
    return True

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        er, ec = q.popleft()
        
        for dr, dc in deltas:
            nr, nc = er + dr, ec + dc

            if can_go(nr, nc):
                q.append((nr, nc))
                visited[nr][nc] = True

bfs(0, 0)
print(1 if visited[n - 1][m - 1] else 0)
