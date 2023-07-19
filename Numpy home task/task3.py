import numpy as np #не стирать!        

def diag_2k(a):
    diag = np.diag(a)

    return sum(diag[diag % 2 == 0])
