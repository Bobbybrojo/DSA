import sys

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Backtracking approach
# First simulate players falling down the ladder and find their positions at the bottom
# Then backtrack on replacing edges one by one 
#   and find the minimum number of edges resulting in the same result

# Returns the results of playing the game with n vertical lines and the given edges
def find_game_results(edges):
    
    # Build a board with 1 based indexing and last row displays player results
    rows = (max([edge[1] for edge in edges]) if len(edges) != 0 else 0) + 2
    board = [
        [0 for _ in range(n + 1)]
        for _ in range(rows)
    ]
    
    # Fill board with edges: 1 represents left side of edge, 2 is right side of edge
    for edge in edges:
        a, b = edge
        board[b][a] = 1
        board[b][a + 1] = 2

    # Simulate ladder game
    for player in range(1, n + 1):

        c = player # current player column
        for r in range(rows):
            if r == rows - 1:
                board[r][c] = player
                continue
            if board[r][c] == 0:
                continue
            elif board[r][c] == 1:
                c += 1
            elif board[r][c] == 2:
                c -= 1

    # Return last row of results of players
    return board[-1]
            
starting_game_results = find_game_results(edges)
min_edges = sys.maxsize

# Backtracking aglorithm
def backtrack(curr_edges, last_idx):
    global min_edges

    # Terminating case: found edges with game results the same as start state
    if find_game_results(curr_edges) == starting_game_results:
        min_edges = min(min_edges, len(curr_edges))
        return
    # Terminating case: number of edges is the same as in starting game
    if len(curr_edges) == m:
        return

    # Backtrack using each edge at most once
    for i in range(last_idx + 1, m):
        edge = edges[i]
        curr_edges.append(edge)
        backtrack(curr_edges, i)
        curr_edges.pop()
            
backtrack([], -1)
print(min_edges)
