from collections import deque

while True:
    n = int(input())
    if n == 0:
        break

    cartas = deque(range(1, n+1))
    discarded_cards = []

    while len(cartas) > 1:
        discarded_cards.append(cartas.popleft())
        cartas.append(cartas.popleft())

    print(f"Discarded cards: {', '.join(map(str, discarded_cards))}")
    print(f"Remaining card: {cartas[0]}")
