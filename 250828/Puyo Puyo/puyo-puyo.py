n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def dfs(r, c, num):
    visited[r][c] = True
    size = 1

    for dr, dc in deltas:
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] == num:
            size += dfs(nr, nc, num)

    return size

visited = [[False] * n for _ in range(n)]
bursting_blocks = 0
max_block = 0
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            block_size = dfs(r, c, grid[r][c])
            if block_size >= 4:
                bursting_blocks += 1
            if block_size > max_block:
                max_block = block_size

print(f'{bursting_blocks} {max_block}')