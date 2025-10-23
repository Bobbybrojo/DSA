from collections import defaultdict

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = defaultdict(list)
for edge in edges:
    v1, v2 = edge
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(root):
    count = 0
    for neighbor in graph[root]:
        if neighbor not in visited:
            visited.add(neighbor)
            count += 1 + dfs(neighbor)
    
    return count

visited = set([1])
num_nodes = dfs(1)
print(num_nodes)