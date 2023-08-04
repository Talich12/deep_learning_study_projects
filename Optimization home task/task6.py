import numpy as np

def numerical_derivative_2d(func, epsilon):
    """
    Function for approximating the gradient of a function with two variables.
    :param func: np.array[2] -> float — arbitrary differentiable function
    :param epsilon: float — maximum increment along each axis
    :return: another function that approximates the gradient at a point
    """
    def grad_func(x):
        """
        :param x: np.array[2] — point at which to calculate the gradient
        :return: np.array[2] — approximate gradient value at the given point
        """
        dx = (func([x[0] + epsilon, x[1]]) - func([x[0] - epsilon, x[1]])) / (2 * epsilon)
        dy = (func([x[0], x[1] + epsilon]) - func([x[0], x[1] - epsilon])) / (2 * epsilon)
        
        return np.array([dx, dy])

    return grad_func


def grad_descent_2d(func, low, high, start=None, callback=None):
    """ 
    Реализация градиентного спуска для функций двух переменных 
    с несколькими локальным минимумами, но известной квадратной окрестностью
    глобального минимума. Все тесты будут иметь такую природу.

    Обратите внимание, что здесь градиент функции не дан.
    Его нужно вычислять приближённо.

    :param func: np.ndarray -> float — функция 
    :param low: левая граница интервала по каждой из осей
    :param high: правая граница интервала по каждой из осей
    """
    eps = 1e-10
    df = numerical_derivative_2d(func, eps)


    if start is None:
        start = np.array([(low[i] + high[i]) / 2 for i in range(2)])

    current_point = start
    learning_rate = 0.5
    num_iterations = 1000

    for _ in range(num_iterations):
        gradient = df(current_point)
        current_point -= learning_rate * gradient

    return current_point

func = lambda x: (
            -1 / ((x[0])**2 + (x[1] - 3)**2 + 1)
            * np.cos(2 * (x[0])**2 + 2 * (x[1] - 3)**2)
        )
low = -5
high = 5
start = np.array([1.1, 3.3])

print(grad_descent_2d(func, low, high, start))
#"answer" : np.array([1, 1.5])