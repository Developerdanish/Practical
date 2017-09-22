def SelSort(L, N):
    for i in range(N):
        sm = L[i]
        pos = i
        for j in range(i+1, N):
            if L[j] < sm:
                sm = L[j]
                pos = j
        L[i], L[pos] = L[pos], L[i]


L = [3, 2, 1]
SelSort(L, len(L))
print L
