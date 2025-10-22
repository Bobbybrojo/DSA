import math
import sys

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Backtrack placing m points from n in the selected_points list C(n, m) times: O(mC(n,m))
def backtrack(curr, last_idx):
    if len(curr) == m:
        selected_points.append(curr[:])
        return

    for i in range(last_idx + 1, n):
        curr.append(points[i])
        backtrack(curr, i)
        curr.pop()
    return

# Get a list of selecting m random points from n total points
selected_points = []
backtrack([], -1)

# Find the minimum distance between the two farthest points of all selected points arrays: O(C(n,m)*m^2)
min_dist = sys.maxsize
for points in selected_points:
    max_dist = 0
    for i in range(0, len(points) - 1):
        for j in range(i, len(points)):
            dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
            if dist > max_dist:
                max_dist = dist

    if max_dist < min_dist:
        min_dist = max_dist

print(min_dist)