n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

def in_range(r, c) -> bool:
    return r >= 1 and c >= 1 and r <= n and c <= n

def move(cr, cc) -> None:
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = cr + dr, cc + dc

        if not in_range(nr, nc) or a[cr][cc] >= a[nr][nc]:
            continue

        return (nr, nc)
    moved = False
    return None

print(a[r][c], end=' ')
while True:
    new_coords = move(r, c)
    if new_coords:
        r, c = new_coords
        print(a[r][c], end=' ')
        continue
    break


