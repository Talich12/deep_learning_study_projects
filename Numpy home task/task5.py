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


