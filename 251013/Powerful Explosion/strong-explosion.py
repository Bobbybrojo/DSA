n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bomb_locs = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            bomb_locs.append((r, c))

bombs = [
    [
        (-2, 0),
        (-1, 0),
        (1, 0),
        (2, 0),
    ],
    [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ],
    [
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1),
    ]
]

def in_range(r, c):
    return r >= 0 and c >= 0 and r < n and c < n

def backtrack(curr, cnt, areas_destroyed):
    global max_areas

    if cnt == len(bomb_locs):
        max_areas = max(max_areas, areas_destroyed)
        # for r in range(n):
        #     for c in range(n):
        #         print(curr[r][c], end=" ")
        #     print()
        # print()
        return

    r, c = bomb_locs[cnt]
    for bomb in bombs:
        placed = set()
        for dr, dc in bomb:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and curr[nr][nc] == 0:
                placed.add((nr, nc))
                curr[nr][nc] = 2

        backtrack(curr, cnt + 1, areas_destroyed + len(placed))

        for pr, pc in placed:
            curr[pr][pc] = 0

max_areas = len(bomb_locs)
backtrack(grid, 0, len(bomb_locs))
print(max_areas)