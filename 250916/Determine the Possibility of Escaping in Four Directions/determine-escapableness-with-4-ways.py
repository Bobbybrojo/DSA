from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def can_go_to(r, c):
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    if graph[r][c] == 0:
        return False
    return True

q = deque([(0, 0)])
while q:
    r, c = q.popleft()

    for dr, dc in deltas:
        nr, nc = r + dr, c + dc

        if can_go_to(nr, nc):
            graph[nr][nc] = 0
            q.append((nr, nc))

print(1 if graph[n - 1][m - 1] == 0 else 0)