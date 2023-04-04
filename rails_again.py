from collections import deque

while True:
    n = int(input())
    if n == 0:
        break

    entrada = input().split()
    saida = input().split()

    pilha = deque()
    i = j = 0

    while True:
        if pilha and j < n and pilha[-1] == saida[j]:
            pilha.pop()
            print("R", end="")
            j += 1
        elif i < n:
            pilha.append(entrada[i])
            print("I", end="")
            i += 1
        else:
            break

    if not pilha:
        print()
    else:
        print(" Impossible")
