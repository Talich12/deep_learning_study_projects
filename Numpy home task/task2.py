import numpy as np

def no_numpy_scalar(v1, v2):
    if len(v1) == len(v2):
        return sum(x*y for x, y in zip(v1, v2))

def numpy_scalar(v1, v2):
    if len(v1) == len(v2):
        return v1.dot(v2)
    
# отлично! так же можно было

# def numpy_scalar (v1, v2):
#     return np.dot(v1, v2)