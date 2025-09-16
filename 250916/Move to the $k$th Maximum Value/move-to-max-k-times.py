from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(lambda x: x - 1, map(int, input().split()))
deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Determines if we can run dfs from the given position and starting num
def can_go_to(r, c, start_num):
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    if grid[r][c] >= start_num:
        return False
    return True

# Bfs returns the next eligible cell to move or (-1, -1) if no eligible cell exists
def find_next_pos(sr, sc):
    start_num = grid[sr][sc]
    next_pos = (-1, -1, -1) # (r, c, value)

    visited = set([(sr, sc)])
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()

        for dr, dc in deltas:
            nr, nc = r + dr, c + dc

            if (nr, nc) not in visited and can_go_to(nr, nc, start_num):
                visited.add((nr, nc))
                q.append((nr, nc))

                # Logic to set next position
                val = grid[nr][nc]
                if val > next_pos[2]:
                    next_pos = (nr, nc, val)
                elif val == next_pos[2]:
                    if nr < next_pos[0]:
                        next_pos = (nr, nc, val)
                    elif nr == next_pos[0] and nc < next_pos[1]:
                        next_pos = (nr, nc, val)

    return next_pos[0:2]

# Track current final position while performing k moves
pos = (r, c)
for _ in range(k):
    nr, nc = pos
    next_pos = find_next_pos(nr, nc)

    if next_pos == (-1, -1):
        break

    pos = next_pos
    
# Print answer
print(pos[0] + 1, pos[1] + 1)
