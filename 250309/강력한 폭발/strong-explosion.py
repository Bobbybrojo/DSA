n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bombs = [
    [
        (-2, 0),
        (-1, 0),
        (1, 0),
        (2, 0),
    ],
    [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ],
    [
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1),
    ]
]

# Determines if the given (r, c) is in the grid
def in_range(r, c):
    return not (r < 0 or c < 0 or r >= n or c >= n)

# Determine if an explosion can occur at the given (r, c)
def can_go(r, c):
    if not in_range(r, c):
        return False
    if grid[r][c] == 1 or grid[r][c] == 2:
        return False
    return True

# Find and store bomb locations
bomb_locations = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            bomb_locations.append((r, c))

def backtrack(bombs_placed, areas_hit):
    global answer
    if bombs_placed == len(bomb_locations):
        answer = max(answer, areas_hit)
        return

    r, c = bomb_locations[bombs_placed]

    # Allow for placement of any bomb
    for bomb in bombs: 
        # place 1's in spaces where explosion hits
        affected = []
        for dr, dc in bomb:
            nr, nc = dr + r, dc + c
            if can_go(nr, nc):
                affected.append((nr, nc))
                grid[nr][nc] = 2

        # Backtrack        
        backtrack(bombs_placed + 1, areas_hit + len(affected))
        
        # Undo explosion cells
        for nr, nc in affected:
            grid[nr][nc] = 0

answer = 0
backtrack(0, 0)

print(answer + len(bomb_locations))

