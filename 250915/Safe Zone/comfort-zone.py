n, m = map(int, input().split())
grid = []
max_k = 0

# Initialize grid with values and find max k value
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    max_k = max(max_k, max(row))

def can_go_to(r, c, k):
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    if grid[r][c] - k <= 0:
        return False
    return True


def dfs(sr, sc, k):
    stack = [(sr, sc)]

    while stack:
        r, c = stack.pop()

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if (nr, nc) not in visited and can_go_to(nr, nc, k):
                visited.add((nr, nc))
                stack.append((nr, nc))


most_safe_zones = (1, 0) # (k, safe_zones) at k where safe zones is maximized
for k in range(1, max_k):
    safe_zones = 0
    visited = set()

    # Find number of safe zones for grid with k rain
    for r in range(n):
        for c in range(m):
            if grid[r][c] - k > 0 and (r, c) not in visited:
                visited.add((r, c))
                safe_zones += 1 
                dfs(r, c, k)

    if safe_zones > most_safe_zones[1]:
        most_safe_zones = (k, safe_zones)

# Print answer
for ans in most_safe_zones:
    print(ans, end=' ')

    