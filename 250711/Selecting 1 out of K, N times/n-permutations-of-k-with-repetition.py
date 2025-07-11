K, N = map(int, input().split())

# Backtracking solution
# All permutations of 1 - K, N Times

curr_perm = []
def permutations():
    if len(curr_perm) == N:
        for elem in curr_perm:
            print(elem, end=" ")
        print()
        return

    for i in range(1, K + 1):
        curr_perm.append(i)
        permutations()
        curr_perm.pop()

permutations()