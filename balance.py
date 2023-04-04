while True:
    try:
        line = input().strip()
    except:
        break

    size = len(line)
    s = []

    for i in range(size):
        if line[i] == '(':
            s.append(i)
        elif line[i] == ')':
            if s and line[s[-1]] == '(':
                s.pop()
            else:
                s.append(i)

    if not s:
        print("correct")
    else:
        print("incorrect")
