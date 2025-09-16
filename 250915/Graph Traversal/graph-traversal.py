n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
adj_list = [[] for _ in range(n + 1)]

for edge in edges:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])

def dfs(root: int):
    neighbors = adj_list[root]
    size = 0

    for neighbor in neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            size += 1 + dfs(neighbor)

    return size

visited = set()
visited.add(1)
print(dfs(1))