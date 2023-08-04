from math import sin, cos, tan, exp, pi, pow

def grad_1(x, y, z):
    #возвращает кортеж из 3 чисел --- частных производных по x,y,z 
    dx = z * cos(x * z) + exp(x)
    dy = -2 * y * z
    dz = x * cos(x * z) - y**2
    return (dx, dy, dz)

print(grad_1(1, 1, 1))