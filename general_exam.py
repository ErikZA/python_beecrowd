while True:
    try:
        N, Q = map(int, input().split())
        cid = []
        while N:
            N -= 1
            cid.append(int(input()))

        cid.sort(reverse=True)

        while Q:
            Q -= 1
            P = int(input())
            print(cid[int(P) - 1])
    except:
        break
