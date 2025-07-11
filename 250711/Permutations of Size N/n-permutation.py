N = int(input())

# Backtracking solution

visited = [False] * (N + 1)
curr = []
def permutations(count):
    if count == N:
        for elem in curr:
            print(elem, end=" ")
        print()
        return

    for num in range(1, N + 1):
        if not visited[num]:
            curr.append(num)
            visited[num] = True

            permutations(count + 1)

            curr.pop()
            visited[num] = False

permutations(0)
