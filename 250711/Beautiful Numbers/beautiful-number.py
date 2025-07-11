N = int(input())

curr = []
def beautiful_numbers():
    global answer
    bn_len = len(curr)

    # Base case
    if bn_len == N:
        answer += 1
        return

    # Termianting case
    if bn_len > N:
        return

    for i in range(1, 4 + 1):
        for _ in range(i):
            curr.append(i)

        beautiful_numbers()

        for _ in range(i):
            curr.pop()


answer = 0
beautiful_numbers()
print(answer)