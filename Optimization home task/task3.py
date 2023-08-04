import numpy as np

def grad_descent_v2(f, df, low=None, high=None, callback=None):

    def find_local_min(f, df, low_local, high_local, iters=5000, lr=0.05):
        #функция для нахождения минимума функции f на промежутке (low_local, high_local)
        x0 = np.random.uniform(low_local, high_local)
        x = x0

        for i in range(iters):
            x = x - lr * 1/np.sqrt(i+1) * df(x)
            x = np.clip(x, low_local, high_local)
        return x

    local = np.linspace(low, high, 6)
    result = np.array([])
    for i in range(len(local) - 2):
        for j in range(10):
            result = np.append(result, find_local_min(f, df, local[i], local[i+1]))

    best_estimate = result[np.argmin(f(result))]

    return best_estimate



f = lambda x: x**6 + x**4 - 10 * x**2 - x
deriv = lambda x: 6 * x**5 + 4 * x**3 - 20 * x - 1
print(grad_descent_v2(f, df=deriv, low=-3, high=3))