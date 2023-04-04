s_y = set()
s_n = set()
a = 0
ans = ''
while True:
    s = input()
    if s == 'FIM':
        break
    if s.__contains__('YES'):
        s_y.add(s.split()[0])
    else:
        s_n.add(s.split()[0])
    if a == 0:
        a = len(s.split()[0])
    elif a < len(s.split()[0]) and s.__contains__('YES'):
        a = len(s.split()[0])
        ans = s.split()[0]
for item in sorted(s_y):
    print(item)
for item in sorted(s_n):
    print(item)
print("\nAmigo do Habay:")
print(ans)
