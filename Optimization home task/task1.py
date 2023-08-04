def numerical_derivative_1d(func, epsilon):

    def deriv_func(x):
        return (func(x + epsilon) - func(x))/epsilon

    return deriv_func