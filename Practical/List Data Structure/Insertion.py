def insert(l, n, data):
    pos = 0
    if data <= l[0]:
        pos = 0
    elif data >= l[n-1]:
        pos = n
    else:
        for i in range(0, n-1):
            if l[i] <= data <= l[i+1]:
                pos = i+1
                break

    l.append(0)
    for i in range(n, pos, -1):
        l[i] = l[i-1]
    l[pos] = data


L = [1, 2, 4, 5]
print L
insert(L, len(L), 3)
print L
