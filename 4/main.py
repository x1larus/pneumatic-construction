import matplotlib.patches
import matplotlib.path
import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera

A_x = -0.353
B_x = 0.353
A_y = B_y = 0.3
C = 3*np.pi / 8
t = 0.01
angle = 3*np.pi / 2
eps = 0.0000001 
tau = 0.9
m = 100
p = 2000
g = 9.8
v = 0
fig, axes = plt.subplots() 
axes.set_aspect("equal") # равномасштабность по x и y, дабы круг не был эллипсом
camera = Camera(fig) 

def calc_f(x):
    # пункт 1.2 тз
    f_x = np.zeros(5, dtype=np.float64)
    f_x[0] = x[0] + x[2]*np.cos(angle - x[3]) - A_x
    f_x[1] = x[1] + x[2]*np.cos(angle + x[4]) - B_x
    f_x[2] = x[2] + x[2]*np.sin(angle - x[3]) - A_y
    f_x[3] = (x[3] + x[4])*x[2] + (x[1] - x[0]) - C
    f_x[4] = x[2] + x[2]*np.sin(angle + x[4]) - B_y
    return f_x

def graphing(x):
    radius1 = ((x[0] - A_x)**2 + (x[2] - A_y)**2)**0.5 #считаем радиус по Пифагору
    radius2 = ((x[1] - B_x)**2 + (x[2] - B_y)**2)**0.5
    plt.plot((A_x, B_x), (A_y, B_y), color = 'black') # крышка (первый массив координаты иксов точек, второй - игреков)
    plt.plot((x[0], x[1]), (0, 0), color = 'black') # пол
                                     # центр     |  высота   | ширина
    circle1 = matplotlib.patches.Arc((x[0], x[2]), 2*radius1, 2*radius1,
                                        0, (angle - x[3])*180/np.pi,    angle*180/np.pi)
                         # угол поворота | угол начала (0 = три часа) | угол конца
    circle2 = matplotlib.patches.Arc((x[1], x[2]), 2*radius2, 2*radius2,
                                        270, 0, x[4]*180/np.pi)
    axes.add_patch(circle1) # добавление фигуры на поле
    axes.add_patch(circle2)
    

# x1 | x2 | y | fi1 | fi2
x = np.zeros(5, dtype=np.float64)

for i in range(250):
    while 1:
        x_next = x - calc_f(x)*tau
        if all(x_next - x < eps):
            break
        x = x_next
    l = x[1] - x[0]
    A_y = A_y + v*t
    B_y = A_y
    v = v + (1/m)*(p*l - m*g)*t
    graphing(x)
    print(x)
    camera.snap()
    for j in range(5):
        x[j] = 0

print("Здесь могла быть ваша реклама")
animation = camera.animate()
animation.save('anime.gif')