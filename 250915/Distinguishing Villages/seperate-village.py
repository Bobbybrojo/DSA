n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Determines if we can run dfs from a position on the grid
def can_go_to(r, c):
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    if grid[r][c] == 0:
        return False
    return True

# Dfs returns the size of the connected component
def dfs(r, c):
    size = 1

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc

        if can_go_to(nr, nc):
            grid[nr][nc] = 0
            size += dfs(nr, nc)

    return size

villages = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            grid[r][c] = 0 # Set position to visited
            size = dfs(r, c) # Get size from dfs

            # Insert initial size into list
            if not villages:
                villages.append(size)
                continue

            # Insert into sorted place in list
            for i in range(0, len(villages)):
                if size <= villages[i]:
                    villages.insert(i, size)
                    break
                if i == len(villages) - 1:
                    villages.append(size)

# Print answer
print(len(villages))
for size in villages:
    print(size)