n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Create n + 1 lists for '1-indexed' nodes
adj_list = [[] for _ in range(n + 2)]

# Fill adjacency list
for v1, v2 in edges:
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

# Implement DFS and find count of vertices reached from node 1
visited = [False] * (n + 1)
vertices_reached = 0

def dfs(v):
    global vertices_reached
    
    # Exclude 1 from the count
    if v != 1:
        vertices_reached += 1

    # Visit adjacent unvisited nodes
    for n in adj_list[v]:
        if not visited[n]:
            visited[n] = True
            dfs(n)

# Visit the first node
visited[1] = True 
dfs(1)
print(vertices_reached)




