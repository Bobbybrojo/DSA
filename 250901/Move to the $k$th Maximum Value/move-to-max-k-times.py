from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

def bfs(sr, sc):

    def can_go(r, c):
        if r < 0 or c < 0 or r >= n or c >= n:
            return False
        if grid[r][c] >= grid[sr][sc]:
            return False
        return True

    visited = [[False] * n for _ in range(n)]
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    max_cell = (-1, -1, -1)

    while q:
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc

            if can_go(nr, nc) and not visited[nr][nc]:
                if grid[nr][nc] > max_cell[2]:
                    max_cell = (nr, nc, grid[nr][nc])
                elif grid[nr][nc] == max_cell[2]:
                    if nr < max_cell[0]:
                        max_cell = (nr, nc, grid[nr][nc]) 
                    elif nr == max_cell[0] and nc < max_cell[1]:
                        max_cell = (nr, nc, grid[nr][nc])
                        
                visited[nr][nc] = True
                q.append((nr, nc))

    return max_cell[0], max_cell[1]


sr, sc = r - 1, c - 1
for _ in range(k):
    new_start = bfs(sr, sc)

    if new_start == (-1, -1):
        break

    sr, sc = new_start

print(f'{sr + 1} {sc + 1}')