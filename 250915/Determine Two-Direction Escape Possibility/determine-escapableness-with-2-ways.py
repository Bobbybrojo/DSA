n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def can_go_to(r, c):
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    if grid[r][c] == 0:
        return False
    return True

def dfs(r, c):
    grid[r][c] = 0

    for dr, dc in [(0, 1), (1, 0)]:
        nr, nc = r + dr, c + dc

        if can_go_to(nr, nc):
            dfs(nr, nc)

dfs(0, 0)

print(1 if grid[n - 1][m - 1] == 0 else 0)