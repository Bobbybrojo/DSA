from collections import deque

n = int(input())
r1, c1, r2, c2 = map(lambda x: x - 1, map(int, input().split()))

# NxN grid visited
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

# Deltas clockwise
deltas = [
    (-2, 1), 
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
]

def can_go(r, c):
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    if visited[r][c]:
        return False
    return True

q = deque()
q.append((r1, c1, 0))

answers = []
def bfs():

    while q:
        r, c, moves = q.popleft()

        if r == r2 and c == c2:
            print(moves)
            exit()

        for i in range(len(deltas)):
            nr, nc = r + deltas[i][0], c + deltas[i][1]

            if can_go(nr, nc):
                visited[nr][nc] = True
                q.append((nr, nc, moves + 1))

                
        

bfs()
print(-1)




