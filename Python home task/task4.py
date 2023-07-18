def cumsum_and_erase(A, erase = 1):
    B = [0]
    for i in A:
        sum = B[-1] + i
        B.append(sum)

    C = B[1::]
    for i in C:
        if i == erase:
            C.remove(i)
    return C