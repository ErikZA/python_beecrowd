# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def compare(a, b):
    x, y = 0, 1
    l, i = 1, 0
    while b:
        q = a//b
        print(q)
        a, b = b, a % b
        x, l = l - q*x, x
        y, i = i - q*y, y

    return a


entradas = int(input())
for _ in range(entradas):
    a, b = map(int, input().split())
    print(compare(a, b))
