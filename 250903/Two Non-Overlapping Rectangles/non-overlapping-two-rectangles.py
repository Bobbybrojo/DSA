import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

rect1 = []
for r1 in range(n - 1):
    for c1 in range(m - 1):
        for r2 in range(r1, n - 1):
            for c2 in range(c1, m - 1):
                rect1.append((r1, c1, r2, c2))

rect2 = []
for r1r1, r1c1, r1r2, r1c2 in rect1:
    for r1 in range(r1r2 + 1, n):
        for r2 in range(r1, n):
            for c1 in range(m):
                for c2 in range(c1, m):
                    rect2.append((r1, c1, r2, c2))

    for c1 in range(r1c2 + 1, m):
        for c2 in range(c1, m):
            for r1 in range(n):
                for r2 in range(r1, n):
                    rect2.append((r1, c1, r2, c2))

def rect_area_sum(rect):
    r1, c1, r2, c2 = rect
    area_sum = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            area_sum += grid[r][c]

    return area_sum

max_sum = -sys.maxsize
for i in range(len(rect1)):
    r1 = rect_area_sum(rect1[i])
    r21 = rect_area_sum(rect2[i])
    r22 = rect_area_sum(rect2[len(rect2) // 2 + i])
    max_sum = max(r1 + r21, r1 + r22, max_sum)

print(max_sum)