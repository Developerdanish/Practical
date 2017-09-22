def BSearch(List, N, Data):
    pos = -1
    LB = 0
    UB = N-1
    while LB <= UB:
        Mid = (LB+UB)/2
        if List[Mid] == Data:
            pos = Mid
            break
        elif Data < List[Mid]:
            LB += 1
        elif Data > List[Mid]:
            UB -= 1
        else:
            pass
    return pos

L = [10,9,8,7,6,5,4,3,2,1]

print BSearch(L, len(L), 4)