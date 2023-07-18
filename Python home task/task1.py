def almost_double_factorial(n):
    if n == 0:
        return 1
    else:
        count = 1
        for i in range(1, n+1):
            if i % 2 == 1:
                count = count * i
        return count
