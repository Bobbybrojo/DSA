n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
er, ec = map(lambda x: x - 1, map(int, input().split()))
size = grid[er][ec]

# First, mark all cells to be removed
to_remove = set()

# Add center
to_remove.add((er, ec))

# Add vertical cells
for i in range(1, size):
    if er - i >= 0:
        to_remove.add((er - i, ec))
    if er + i < n:
        to_remove.add((er + i, ec))

# Add horizontal cells  
for i in range(1, size):
    if ec - i >= 0:
        to_remove.add((er, ec - i))
    if ec + i < n:
        to_remove.add((er, ec + i))

# Process each column
for c in range(n):
    temp = []
    for r in range(n):
        if (r, c) not in to_remove:
            temp.append(grid[r][c])
    
    # Add zeros at the top (gravity effect)
    temp = [0] * (n - len(temp)) + temp
    
    # Place back in grid
    for r in range(n):
        grid[r][c] = temp[r]

for r in range(n):
    for c in range(n):
        print(grid[r][c], end=' ')
    print()