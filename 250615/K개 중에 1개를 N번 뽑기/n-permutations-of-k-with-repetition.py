K, N = map(int, input().split())

def print_answer():
    for e in answer:
        print(e, end=" ")
    print()

answer = []
def choose(curr):
    if curr == N:
        print_answer()
        return

    for i in range(1, K + 1):
        answer.append(i)
        choose(curr + 1)
        answer.pop()

choose(0)