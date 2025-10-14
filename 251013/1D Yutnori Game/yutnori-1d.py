n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

def backtrack(curr):
    global max_score

    # Recursion base case
    if len(curr) == len(nums):

        # Tally amount of points earned for pieces chosen to move
        positions = [1 for _ in range(k)]
        awarded_point = set()
        points = 0
        for i in range(len(curr)):
            piece = curr[i]
            positions[piece] += nums[i]

            # Clamp value
            if positions[piece] > m:
                positions[piece] = m

            # Add points
            if positions[piece] == m and piece not in awarded_point:
                points += 1
                awarded_point.add(piece)

        # Track max points seen
        max_score = max(max_score, points)
        return

    # Select a piece to move and backtrack
    for i in range(0, k):
        curr.append(i)
        backtrack(curr)
        curr.pop()

max_score = 0
backtrack([])
print(max_score)