import heapq as hq

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]

cc_sizes = []


def can_go(r: int, c: int):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False
    if grid[r][c] != 1:
        return False
    return True

# Dfs identifies the size of a connected component, marks it as seen
def dfs(r: int, c: int) -> None:
    grid[r][c] = 2 # Mark self as visited
    size = 1

    for dr, dc in deltas:
        nr, nc = r + dr, c + dc
        if can_go(nr, nc):
            size += dfs(nr, nc)

    return size

for r in range(n):
    for c in range(n):
        if grid[r][c] == 2: # Position already seen
            continue
        elif grid[r][c] == 1: # Connected component here: run dfs
            hq.heappush(cc_sizes, dfs(r, c))
        else:
            grid[r][c] = 2 # Nothing here, mark it as seen

print(len(cc_sizes))
while cc_sizes:
    print(hq.heappop(cc_sizes))