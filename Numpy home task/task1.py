import numpy as np

def no_numpy_mult(first, second):
    result = []
    for i in range(len(first)):
        result_row = []
        for j in range(len(second[0])):
            result_ij = sum(first[i][k] * second[k][j] for k in range(len(first)))
            result_row.append(result_ij)
        result.append(result_row)
    
    return result

def numpy_mult(first, second):
    return first.dot(second)

# отлично )
#  еще можно было 

# def numpy_mult(first, second):
#     return np.dot(first, second)