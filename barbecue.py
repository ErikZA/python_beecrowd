while True:
    try:
        t = int(input())
    except:
        break

    x = []
    for i in range(t):
        h, j = input().split()
        j = int(j)
        x.append((h, j))

    for i in range(len(x)):
        for ptr in range(len(x)-i-1):
            if x[ptr][1] > x[ptr+1][1]:
                x[ptr], x[ptr+1] = x[ptr+1], x[ptr]

    for i in range(len(x)-1):
        print(x[i][0], end=' ')
    print(x[-1][0])
