n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Return if dfs can run from the position given the block number
def can_go_to(r, c, num):
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    if grid[r][c] != num or (r, c) in visited:
        return False
    return True

def dfs(r, c):
    size = 1
    num = grid[r][c]
    
    for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if can_go_to(nr, nc, num):
            visited.add((nr, nc))
            size += dfs(nr, nc)
    
    return size

visited = set()
bursting_blocks = 0
largest_block = 0

for r in range(n):
    for c in range(n):
        visited.add((r, c))
        block_size = dfs(r, c)

        if block_size >= 4:
            bursting_blocks += 1

        if block_size > largest_block:
            largest_block = block_size

print(bursting_blocks, largest_block)