def delete(l, n, data):
    pos = -1
    for j in range(n):
        if data == l[j]:
            pos = j
            break
    if pos >= 0:
        for i in range(pos, n-1):
            l[i] = l[i+1]
    return pos


L = [1, 2, 3, 4, 5]
print L
delete(L, len(L), 3)
print L
