n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


# THIRD Attempt: Greedy: O(n^4)
# Select the maximum number on the grid
# Then select the next maximum number not in previous r, c
# perform this n times


result = 0
starting_rc = [[False] * n for _ in range(n)]
# Perform n times
for _ in range(n):
    visited_rows = [False] * n
    visited_cols = [False] * n
    some_sum = 0
    # Find n elements
    for i in range(n):
        max_elem_pos = (0, 0)
        max_val = 0
        # Search through grid for the next max
        for r in range(n):
            if visited_rows[r]:
                continue

            for c in range(n):
                if visited_cols[c]:
                    continue

                if i == 0 and starting_rc[r][c]:
                    continue

                if grid[r][c] > max_val:
                    max_val = grid[r][c]
                    max_elem_pos = (r, c)

        if i == 0:
            starting_rc[max_elem_pos[0]][max_elem_pos[1]] = True
        visited_rows[max_elem_pos[0]] = True
        visited_cols[max_elem_pos[1]] = True
        some_sum += grid[max_elem_pos[0]][max_elem_pos[1]]
    
    result = max(result, some_sum)

print(result)
        
            



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

##############################################

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
