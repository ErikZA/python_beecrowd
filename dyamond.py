n = int(input())

for i in range(n):
    linha = input().strip()
    esq = 0
    dir = 0
    for j in range(len(linha)):
        if linha[j] == '<':
            esq += 1
        elif linha[j] == '>':
            if esq > 0:
                dir += 1
                esq -= 1
    print(dir)
