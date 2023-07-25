import numpy as np

def cumsum(A):
    result = []
    for row in A:
        row = np.array(row)
        result.append(row.cumsum())
    return result

# Отлично )
# Еще можно указать вдоль какой оси массива (тензора) мы хотим выполнить преобразование.
# В numpy по возможности лучше всего избегать циклов.
# Нужно стараться делать все матрично, так работает наиболее быстро и эффективно.
#  Задание сравнить время работы своего варианта и полностью матричного ниже )

# def cumsum(A):
#     #param A: np.array[m,n]
#     return np.cumsum(A, axis = 1)
