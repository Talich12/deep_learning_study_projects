import numpy as np

def transform(X, a=1):
    result = []
    for row in X:
        reference = np.array(row)
        row = np.array(row)
        row[1::2] = a
        row[::2] = row[::2]**3
        row = row[::-1]
        result.append(np.hstack((reference, row)))
    result = np.array(result)
    return result

# Отлично ) Ниже красивое решение повторяет алгоритм описанный в задании МФТИ.

# def transform(X, a=1):
#     Y = X.copy()
#     Y[:, 1::2] = a
#     Y[:, ::2] **= 3
#     Y = Y[:, ::-1]
#     return np.concatenate((X, Y), axis=1)

