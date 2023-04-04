stdent = int(input())
code = []
note = []
max_note = 0.0

for i in range(stdent):
    c, n = map(float, input().split())
    code.append(int(c))
    note.append(n)
    if n > max_note:
        max_note = n
        final_code = int(c)

if max_note < 8:
    print("Minimum note not reached")
else:
    print(final_code)
