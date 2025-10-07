import sys

n = int(input())
a = list(map(int, input().split()))

max_sum = -sys.maxsize
curr_sum = 0
for i in range(n):
    curr_sum += a[i]

    max_sum = max(max_sum, curr_sum)

    if curr_sum < 0:
        curr_sum = 0

print(max_sum)