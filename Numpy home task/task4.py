import numpy as np

def cumsum(A):
    result = []
    for row in A:
        row = np.array(row)
        result.append(row.cumsum())
    return result
