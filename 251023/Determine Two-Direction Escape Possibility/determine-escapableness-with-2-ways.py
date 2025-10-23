n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(1, 0), (0, 1)]
def in_range(r, c):
    return r < n and r >= 0 and c < m and c >= 0

def dfs(r, c, visited):
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] != 0:
            visited[nr][nc] = True
            dfs(nr, nc, visited)
    return visited[n - 1][m - 1]

result = dfs(0, 0, [[False] * m for _ in range(n)])
print(1 if result else 0)