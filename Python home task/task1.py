def almost_double_factorial(n):
    if n == 0:
        return 1
    else:
        count = 1
        for i in range(1, n+1):
            if i % 2 == 1:
                count = count * i
        return count
    
# все правильно, просто есть еще интересный подход
# в функциональном стиле
# from functools import reduce

# def almost_double_factorial(n):
#     if n:
#         return reduce(lambda x, y: x * y, range(1, n + 1, 2))
#     else:
#         return 1

