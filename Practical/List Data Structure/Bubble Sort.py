def bsort(l, N):
    for i in range(N):
        for j in range(N-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


L = [3, 2, 1]
bsort(L, len(L))
print L
