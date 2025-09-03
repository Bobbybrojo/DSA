import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

rects = []
for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                rects.append((r1, c1, r2, c2))

def rect_area_sum(rect):
    r1, c1, r2, c2 = rect
    area_sum = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            area_sum += grid[r][c]

    return area_sum

def rects_overlap(rect1, rect2):
    r1a, c1a, r2a, c2a = rect1
    r1b, c1b, r2b, c2b = rect2

    return not (r2a < r1b or r2b < r1a or c2a < c1b or c2b < c1a)

max_sum = -sys.maxsize
for i in range(len(rects)):
    for j in range(i + 1, len(rects)):
        if not rects_overlap(rects[i], rects[j]):
            max_sum = max(max_sum, rect_area_sum(rects[i]) + rect_area_sum(rects[j]))

print(max_sum)