n = int(input())
segments = []

for _ in range(n):
    a, b = map(int, input().split())
    segments.append((a, b))

# Backtracking approach
# sort inputs by start time
# Select inputs one by one and find the combination without overlaps

segments.sort()

def overlapping(s1, s2):
    return s1[1] >= s2[0]

ans = 0
def backtrack(curr, last_idx):
    global ans
    if last_idx == n - 1:
        ans = max(ans, len(curr))
    
    for i in range(last_idx + 1, n):
        if len(curr) != 0 and overlapping(curr[-1], segments[i]):
            continue
        curr.append(segments[i])
        backtrack(curr, i)
        curr.pop()

backtrack([], -1)
print(ans)