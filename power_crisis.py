# Esse algoritmo resolve o problema de Josefo, que é um problema matemático que funciona da seguinte forma:
# há n pessoas em pé em um círculo e queremos eliminar a proxima pessoa, dando a volta no círculo no sentido horário,
# até que reste apenas uma pessoa. O problema é encontrar a posição da última pessoa restante.

# Logo a saida é 1 pois é o numero minimo de deslocamento necessario para encontrar a região 13.

# Simula a queda de energia em um circulo de regioes
# n: numero de regioes do circulo
# k: numero de deslocamentos necessarios para pular uma regiao do circulo
# retorna True se a regiao 13 for a ultima regiao a ser removida do circulo
def josephus(n, k):
    index = 0  # inice da regiao a ser pulada
    v = list(range(1, n+1))  # lista de regioes do circulo

    while len(v) > 1:
        del v[index]  # remove a regiao a ser pulada
        # calcula a proxima regiao a ser pulada
        index = (index + k - 1) % len(v)

        # a logica do laço é:
        # a cada interação remover sempre o item seguinte do array v e atualizar o indice para a proxima regiao a ser removida
        # exemplo:
        # n = 13, k = 1
        # v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # index = 0
        # remove o item 0 do array v e atualiza o index para o proximo item
        # index = (0 + 1 - 1) % 13 = 0
        # na proxima interação o item 0 do array v será removido novamente
        # v = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # index = 0
        # remove o item 0 do array v e atualiza o index para o proximo item
        # index = (0 + 1 - 1) % 12 = 0
        # na proxima interação o item 0 do array v será removido novamente
        # e assim por diante até que o array v tenha apenas um item
        # v = [13]
        # que é o a região que deve ser retornada

    return v[0] == 13


def main():
    while True:
        # A entrada minima é 13 pois é o numero de regioes que o problema trabalha.
        line = int(input())  # o numero de regioes do circulo
        if line == 0:  # se a entrada for 0 o programa deve ser encerrado
            break

        ans = 1  # o numero minimo de deslocamentos necessarios para garantir que a regiao 13 não foi desligada
        # pois a regiao 13 deve ser a ultima a ser desligada
        # enquanto o josephus não retornar o valor 13 não é possivel garantir que a regiao 13 não foi desligada
        while not josephus(line, ans):
            ans += 1
        print(ans)


main()


# exemplo de entrada: 14

# a cada interação remover sempre o item seguinte do array v e atualizar o indice para a proxima regiao a ser removida
# exemplo:
# primeira interação josephus(14, 1)
# # n = 14, k = 1
# v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# index = 0
# remove o item 0 do array v e atualiza o index para o proximo item
# index = (0 + 1 - 1) % 14 = 0
# na proxima interação o item 0 do array v será removido novamente
# v = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# index = 0
# remove o item 0 do array v e atualiza o index para o proximo item
# index = (0 + 1 - 1) % 13 = 0
# na proxima interação o item 0 do array v será removido novamente
# e assim por diante até que o array v tenha apenas um item que é 14
# NãO é possivel garantir que a regiao 13 não foi desligada pois a regiao 13 não é a ultima a ser desligada
#
# segunda interação josephus(14, 2)
# # n = 14, k = 2
# v = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# index = 0
# remove o item 0 do array v e atualiza o index para o proximo item
# index = (0 + 2 - 1) % 14 = 1
# na proxima interação o item 1 do array v será removido
# v = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# index = 1
# remove o item 1 do array v e atualiza o index para o proximo item
# index = (1 + 2 - 1) % 13 = 2
# na proxima interação o item 2 do array v será removido
# v = [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# index = 2
# remove o item 2 do array v e atualiza o index para o proximo item
# index = (2 + 2 - 1) % 12 = 3
# na proxima interação o item 3 do array v será removido
# v = [2, 4, 6, 8, 9, 10, 11, 12, 13, 14]
# index = 3
# remove o item 3 do array v e atualiza o index para o proximo item
# index = (3 + 2 - 1) % 11 = 4
# na proxima interação o item 4 do array v será removido
# v = [2, 4, 6, 8, 10, 11, 12, 13, 14]
# index = 4
# remove o item 4 do array v e atualiza o index para o proximo item
# index = (4 + 2 - 1) % 10 = 5
# na proxima interação o item 5 do array v será removido
# v = [2, 4, 6, 8, 10, 12, 13, 14]
# index = 5
# remove o item 5 do array v e atualiza o index para o proximo item
# index = (5 + 2 - 1) % 9 = 6
# na proxima interação o item 6 do array v será removido
# v = [2, 4, 6, 8, 10, 12, 14]
# index = 6
# remove o item 6 do array v e atualiza o index para o proximo item
# index = (6 + 2 - 1) % 8 = 7
# na proxima interação o item 7 do array v será removido
# v = [2, 4, 6, 8, 10, 12, 14]
# index = 7
# remove o item 7 do array v e atualiza o index para o proximo item
# index = (7 + 2 - 1) % 7 = 1
# na proxima interação o item 0 do array v será removido novamente
# Aqui é quando o circulo de regioes se fecha novamente.

# assim por diante ele segue interando ans até que o josephus retorne True
