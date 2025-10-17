from collections import deque

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(lambda x: x - 1, map(int, input().split()))

# Index to Change in Direction mapping for move_dir
dirs = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# Tells if a row and col are in range of the grid
def in_range(r, c):
    return r >= 0 and c >= 0 and r < n and c < n

# DFS with memoization
memo = [[-1] * n for _ in range(n)]
def dfs(r, c):
    if memo[r][c] != -1:
        return memo[r][c]

    curr_num = num[r][c]
    mdir = move_dir[r][c]
    direction = dirs[mdir]

    max_from_here = 0
    nr, nc = r + direction[0], c + direction[1]
    while in_range(nr, nc):
        if num[nr][nc] > curr_num:
            max_from_here = max(max_from_here, 1 + dfs(nr, nc))
        nr += direction[0]
        nc += direction[1]

    memo[r][c] = max_from_here
    return max_from_here

print(dfs(sr, sc))