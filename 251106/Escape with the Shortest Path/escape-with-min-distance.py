from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# Tells if the coordinates are valid position to move to
def can_go_to(r, c):
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    if a[r][c] == 0:
        return False
    return True

# Use BFS to find shortest distance
def bfs():
    
    #        r, c, depth
    start = (0, 0, 0)
    q = deque([start])
    while q:
        r, c, depth = q.popleft()

        if r == n - 1 and c == m - 1:
            return depth

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if can_go_to(nr, nc):
                a[nr][nc] = 0
                q.append((nr, nc, depth + 1))

print(bfs())