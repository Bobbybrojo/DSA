N = int(input())


answer = 0
curr = []
def beautiful_numbers(n):
    global answer
    if n == N:
        answer += 1
        return
    elif n > N:
        return
    
    # Select a number from 1 to 4
    for selection in range(1, 4 + 1):
        for _ in range(selection):
            curr.append(selection)
        
        beautiful_numbers(n + selection)

        for _ in range(selection):
            curr.pop()


beautiful_numbers(0)
print(answer)