import sys


def josephus(n, k):
    index = 0
    v = list(range(1, n+1))

    while len(v) > 1:
        del v[index]
        index = (index + k - 1) % len(v)

    return v[0] == 13


def main():
    while True:
        line = int(input())
        if line == 0:
            break

        ans = 1
        while not josephus(line, ans):
            ans += 1
        print(ans)


main()
