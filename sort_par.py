n = int(input())
par = []
impar = []

for i in range(n):
    a = int(input())
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)

par.sort()
impar.sort(reverse=True)

for i in range(len(par)):
    print(par[i])
for i in range(len(impar)):
    print(impar[i])
