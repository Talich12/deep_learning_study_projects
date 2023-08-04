from math import sin, cos, tan, exp, sqrt, pi
def grad_2(x, y, z):
    #возвращает кортеж из 3 чисел --- частных производных по x,y,z 
    dx = -exp(x+y) * (sin(exp(x+y))/cos(exp(x+y))) - 1/x
    dy = -exp(x+y) * (sin(exp(x+y))/cos(exp(x+y))) - 1/y
    dz = 0
    return (dx, dy, dz)

print(grad_2(1, 1, 0))