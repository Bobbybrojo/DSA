import sys

n = int(input())
grid = [list(input()) for _ in range(n)]

# Runtime C(n, 3) + n^2 -> Overall O(n^2) for finding node positions
# Find positions of start, end, and digits O(n^2)
# Sort the positions from low number to high number O(nlog(n))
# Approach use backtracking to find all 3 coin movement combinations
# Calculate # of steps to move between coins for each combination and find the min

# Find coin all 3 coin combinations and store them in combinations list
def backtrack(curr, last_idx):
    if len(curr) == 3: # 3 coins
        combinations.append(curr[:])
        return

    # Perform backtracking on nodes greater than previous nodes
    for i in range(last_idx + 1, len(nodes)):
        node = nodes[i]
        curr.append(node)
        backtrack(curr, i)
        curr.pop()

    return
    

# Find all nodes and sort them in ascending order 1-9
start = (0, -1, -1)
end = (10, -1, -1)
nodes = []
for r in range(n):
    for c in range(n):
        value = grid[r][c]
        if value == "S":
            start = (0, r, c)
        elif value == "E":
            end = (10, r, c)
        elif value != ".":
            nodes.append((int(value), r, c))
nodes.sort()

# Perform backtracking to fill combinations list
combinations = []
backtrack([], -1)

min_steps = sys.maxsize

# For each combination, calculate number of steps through each node and update min_steps
for comb in combinations:
    if len(comb) < 3:
        continue

    comb.append(end)
    steps = 0
    curr_pos = start
    for pos in comb:
        steps += (abs(curr_pos[1] - pos[1]) + abs(curr_pos[2] - pos[2]))
        curr_pos = pos

    if steps < min_steps:
        min_steps = steps

print(min_steps if min_steps != sys.maxsize else -1)
    