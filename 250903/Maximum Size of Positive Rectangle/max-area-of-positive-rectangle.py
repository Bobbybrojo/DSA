n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def positive_rect(rect):
    r1, c1, r2, c2 = rect

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] <= 0:
                return False

    return True

max_area = -1
for r1 in range(n):
    for r2 in range(r1, n):
        for c1 in range(m):
            for c2 in range(c1, m):
                if positive_rect((r1, c1, r2, c2)):
                    max_area = max((r2 - r1 + 1) * (c2 - c1 + 1), max_area)    

print(max_area)