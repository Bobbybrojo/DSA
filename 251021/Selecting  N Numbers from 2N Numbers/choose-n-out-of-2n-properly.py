import sys

n = int(input())
num = list(map(int, input().split()))
num_set = set(num)

# Approach: backtracking
# find all combinations of n numbers from 2n total
# then compare difference with sum of combination and 
# sum of set diff of num list and combination

def backtracking(curr, last_idx):
    if len(curr) == n:
        partitions.append(curr[:])
        return

    for i in range(last_idx + 1, 2 * n):
        value = num[i]
        curr.append(value)
        backtracking(curr, i)
        curr.pop()
    return

# Fill the partitions list
partitions = []
backtracking([], -1)

# Find the min difference from the partitions
min_diff = sys.maxsize
for p1 in partitions:
    p2 = num_set - set(p1)
    min_diff = min(min_diff, (abs(sum(p1) - sum(p2))))
print(min_diff)
