K, N = map(int, input().split())

# Please write your code here.


curr = []
def perm(n):
    if n == 0:
        for e in curr:
            print(e, end=' ')
        print()
        return
    
    for selection in range(1, K + 1):
        curr.append(selection)
        perm(n - 1)
        curr.pop()

perm(N)