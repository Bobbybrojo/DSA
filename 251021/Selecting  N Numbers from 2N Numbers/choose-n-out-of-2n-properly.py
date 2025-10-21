import sys

n = int(input())
num = list(map(int, input().split()))

# Approach: backtracking
# Partition the numbers into two running lists by alternating adding to each list

def backtracking(curr1, curr2, cnt):
    global min_diff

    if len(curr1) == n and len(curr2) == n:
        min_diff = min(min_diff, abs(sum(curr1) - sum(curr2)))
        return

    for i in range(0, 2 * n):
        value = num[i]
        if i not in visited:
            visited.add(i)

            if cnt % 2 == 0:
                curr1.append(value)
                backtracking(curr1, curr2, cnt + 1)
                curr1.pop()
            else: # cnt % 2 == 1
                curr2.append(value)
                backtracking(curr1, curr2, cnt + 1)
                curr2.pop()

            visited.remove(i)

visited = set()
min_diff = sys.maxsize
backtracking([], [], 0)
print(min_diff)
