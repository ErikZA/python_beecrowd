from collections import deque


def bfs(estado_inicial):
    fila = deque([(estado_inicial, 0)])
    visitados = []

    while fila:
        estado_atual, profundidade = fila.popleft()

        if estado_atual not in visitados:
            visitados.append(estado_atual)

            if objetivo_alcancado(estado_atual):
                return estado_atual, profundidade

            for proximo_estado in gerar_proximos_estados(estado_atual):
                fila.append((proximo_estado, profundidade + 1))

    return estado_atual, profundidade


def gerar_proximos_estados(estado_atual):
    # Encontra a posição da peça vazia
    posicao_vazia = estado_atual.index(None)

    # Lista para armazenar os próximos estados
    proximos_estados = []

    # Verifica se é possível mover a peça à esquerda
    if posicao_vazia % 2 != 0 and posicao_vazia > 0:
        novo_estado = estado_atual.copy()
        novo_estado[posicao_vazia], novo_estado[posicao_vazia -
                                                1] = novo_estado[posicao_vazia - 1], novo_estado[posicao_vazia]
        proximos_estados.append(novo_estado)

    # Verifica se é possível mover a peça à direita
    if posicao_vazia % 2 != 1 and posicao_vazia < len(estado_atual) - 1:
        novo_estado = estado_atual.copy()
        novo_estado[posicao_vazia], novo_estado[posicao_vazia +
                                                1] = novo_estado[posicao_vazia + 1], novo_estado[posicao_vazia]
        proximos_estados.append(novo_estado)

    # Verifica se é possível mover a peça para cima
    if posicao_vazia >= 2:
        novo_estado = estado_atual.copy()
        novo_estado[posicao_vazia], novo_estado[posicao_vazia -
                                                2] = novo_estado[posicao_vazia - 2], novo_estado[posicao_vazia]
        proximos_estados.append(novo_estado)

    # Verifica se é possível mover a peça para baixo
    if posicao_vazia <= len(estado_atual) - 3:
        novo_estado = estado_atual.copy()
        novo_estado[posicao_vazia], novo_estado[posicao_vazia +
                                                2] = novo_estado[posicao_vazia + 2], novo_estado[posicao_vazia]
        proximos_estados.append(novo_estado)

    return proximos_estados


def objetivo_alcancado(estado):
    return all(estado[i] == 'A' for i in range(len(estado)//2))


# Teste
estado_inicial = [None, 'V', 'V', 'A', 'A', 'V', 'V', 'A', 'A', 'V']
print(bfs(estado_inicial))
