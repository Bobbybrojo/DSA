n = int(input())

# Visited array for backtracking
visited = [False] * (n + 1)

def perm(curr):
    if len(curr) == n:
        for elem in curr:
            print(elem, end=" ")
        print()
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            curr.append(i)

            perm(curr)

            visited[i] = False
            curr.pop()
    return

# Print all permutations of 1 to N
perm([])