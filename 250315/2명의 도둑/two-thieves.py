n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Calculate the value of a set of ranges
def calculate_value(ranges):

    # Backtracking algorithm to find maximum value by selecting valid cells from range
    def backtrack(curr, last_idx, cnt):
        nonlocal max_value
        curr_val = sum(map(lambda x: x**2, curr))
        max_value = max(max_value, curr_val)

        # Select unique elements in the range to check
        for i in range(last_idx, r[1] + 1):
            if weight[r[2]][i] + cnt > c:
                continue
            curr.append(weight[r[2]][i])
            backtrack(curr, i + 1, cnt + weight[r[2]][i])
            curr.pop()

    # For each range, select elements with maximum weight not exceeding c
    total_value = 0
    for r in ranges:
        max_value = 0
        backtrack([], r[0], 0)
        total_value += max_value

    return total_value

# Check if a range is valid considering previous ranges used
def range_valid(ranges, rng):
    if len(ranges) == 0:
        return True
    
    # Check all (1) ranges against new range for collisions
    for r in ranges:
        if r[2] == rng[2] and not (r[1] < rng[0] or rng[1] < r[0]):
            return False
    return True
    

max_value = 0

# Backtracking algorithm
def backtrack(ranges):
    global max_value

    # Terminating condition: Calculate value of ranges with backtracking once hit
    if len(ranges) == 2:
        curr_value = calculate_value(ranges)
        max_value = max(max_value, curr_value)
        return

    for r in range(n): # Select Row
        for start in range(0, n - m + 1): # Select range in row
            end = start + m - 1
            rng = (start, end, r) # inclusive range of items picked

            if range_valid(ranges, rng):
                ranges.append(rng)
                backtrack(ranges)
                ranges.pop()

backtrack([])
print(max_value)

