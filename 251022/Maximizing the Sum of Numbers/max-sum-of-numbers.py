n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


# THIRD SOLUTION: Optimized backtracking (Only backtrack on possible solutions)
# Runtime: O(P(n^2, n) * n)
visited_col = [False] * n
visited_row = [False] * n

def backtracking(curr):
    global max_sum

    if len(curr) == n:
        max_sum = max(max_sum, sum(curr)) # O(n) for summing list for each result
        return

    for c in range(n):
        if visited_col[c]:
            continue

        for r in range(n):
            if visited_row[r]:
                continue
            
            visited_row[r] = True
            visited_col[c] = True
            curr.append(grid[r][c])          

            backtracking(curr)

            visited_row[r] = False
            visited_col[c] = False
            curr.pop()
    return

max_sum = -1
backtracking([])
print(max_sum)


# RESULT: Does not cover the entire solution space
# SECOND SOLUTION: Result: Faster Overall
# Ad hoc: simulate a diagonal on the grid and move it once to the right for each permutation
# Use modulo to wrap chosen column
# Presumed runtime O(n^2)

# max_sum = -1
# visited = [False] * n
# for r in range(n):
#     curr = []
#     for c in range(n):
#         if visited[c]:
#             continue

#         curr.append(grid[r][c])

#     max_sum = max(max_sum, sum(curr))
#     print(curr, sum(curr))
# print(max_sum)

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
