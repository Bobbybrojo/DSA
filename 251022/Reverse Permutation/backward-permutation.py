n = int(input())

# Visited array
visited = [False] * (n + 1)

# Reverse Permutation function
def perm(curr):
    if len(curr) == n:
        for elem in curr:
            print(elem, end=" ")
        print()
        return

    for i in range(n, 0, -1):
        if not visited[i]:
            # Add i to permutation
            visited[i] = True
            curr.append(i)
            
            # Backtrack
            perm(curr)

            # Remove i from permutation
            visited[i] = False
            curr.pop()
    return

perm([])