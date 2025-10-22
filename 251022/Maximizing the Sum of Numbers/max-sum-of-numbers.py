n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


# SECOND SOLUTION: Result: Faster Overall
# Ad hoc: simulate a diagonal on the grid and move it once to the right for each permutation
# Use modulo to wrap chosen column
# Presumed runtime O(n^2)

max_sum = -1
c = 0
for start in range(n):
    curr = []
    for r in range(start, n + start):
        curr.append(grid[r % n][c % n])
        c += 1
    max_sum = max(max_sum, sum(curr))
print(max_sum)

# FIRST SOLUTION
# Brute force backtracking: O(P(n, n) * n) : PASSES
# visited_rows = [False] * n

# def backtracking(curr, cnt):
#     if len(curr) == n:
#         perms.append(curr[:])
#         return

#     for r in range(n):
#         if not visited_rows[r]:
#             visited_rows[r] = True
#             curr.append(grid[r][cnt])
            
#             backtracking(curr, cnt + 1)

#             visited_rows[r] = False
#             curr.pop()
#     return

# perms = []
# backtracking([], 0)

# max_sum = -1
# for perm in perms:
#     max_sum = max(max_sum, sum(perm))
# print(max_sum)
