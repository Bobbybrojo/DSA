n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
deltas = [(1, 0), (0, 1)]

def can_go(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return False
    if grid[r][c] == 0:
        return False
    return True

def dfs(r, c):
    visited[r][c] = True
    
    for dr, dc in deltas:
        nr, nc = r + dr, c + dc

        if can_go(nr, nc) and not visited[nr][nc] :
            dfs(nr, nc)

dfs(0, 0)
print(1 if visited[n - 1][m - 1] else 0)