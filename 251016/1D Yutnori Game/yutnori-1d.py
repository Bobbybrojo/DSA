from collections import defaultdict

n, m, k = map(int, input().split())
moves = list(map(int, input().split()))

# Backtracking Brute Force approach

def backtrack(curr, cnt):
    global max_score

    # Recursion base case
    if cnt == len(moves):
        points = 0
        
        # Tally amount of points earned for pieces chosen to move
        for i in range(len(curr)):
            if curr[i] >= m:
                points += 1

        # Track max points seen
        max_score = max(max_score, points)
        return

    # Select a piece to move and backtrack
    for i in range(0, k):
        curr[i] += moves[cnt]

        backtrack(curr, cnt + 1)

        curr[i] -= moves[cnt]

max_score = 0
backtrack([1 for _ in range(k)], 0)
print(max_score)