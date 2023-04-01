import matplotlib.patches
import matplotlib.path
import matplotlib.pyplot as plt
import numpy as np

A_x = -0.353
B_x = 0.353
A_y = B_y = 0.3
C = 3*np.pi / 8
t = 0.1
angle = 3*np.pi / 2
eps = 0.00001

def calc_f(x):
    # пункт 1.2 тз
    f_x = np.zeros(5, dtype=np.float64)
    f_x[0] = x[0] + x[2]*np.cos(angle - x[3]) - A_x
    f_x[1] = x[1] + x[2]*np.cos(angle + x[4]) - B_x
    f_x[2] = x[2] + x[2]*np.sin(angle - x[3]) - A_y
    f_x[3] = (x[3] + x[4])*x[2] + (x[1] - x[0]) - C
    f_x[4] = x[2] + x[2]*np.sin(angle + x[4]) - B_y
    return f_x

# x1 | x2 | y | fi1 | fi2
x = np.zeros(5, dtype=np.float64)

for i in range(100):
    x_next = x - calc_f(x)
    if all(x_next - x < eps):
        break
    x = x_next

# graphing
print("Здесь могла быть ваша реклама")