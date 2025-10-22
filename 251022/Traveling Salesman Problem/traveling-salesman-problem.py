import sys

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# backtracking: O(nP(n,n))
def backtrack(curr_sum, prev_idx, cnt):
    global min_sum

    if cnt == n:
        if A[prev_idx][0] != 0:
            total_cost = curr_sum + A[prev_idx][0]
            min_sum = min(min_sum, total_cost)
        return

    for i in range(0, n):
        if not visited[i] and A[prev_idx][i] != 0:
            visited[i] = True
            backtrack(curr_sum + A[prev_idx][i], i, cnt + 1)
            visited[i] = False
    return


# Calculate min cost from all permutations
visited = [False] * n
visited[0] = True
min_sum = sys.maxsize
backtrack(0, 0, 1)

print(min_sum)