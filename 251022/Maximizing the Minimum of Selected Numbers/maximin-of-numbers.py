n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Backtrack and track current min throughout function: O(P(n, n))
def backtracking(curr_min, cnt):
    global result

    if cnt == n:
        result = max(result, curr_min)
        return
    
    for r in range(n):
        if not visited[r]:
            visited[r] = True
            if curr_min == None:
                curr_min = grid[r][cnt]
            backtracking(min(curr_min, grid[r][cnt]), cnt + 1)
            visited[r] = False
    return

visited = [False] * n
result = -1
backtracking(None, 0)
print(result)
