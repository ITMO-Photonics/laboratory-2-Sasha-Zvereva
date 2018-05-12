import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()#задаем фигуру

point, = ax.plot([], [], 'bo', ms = 15 )#шарик
coord = np.array([10.,8.])#координата начала движения
v = np.array([0.,0.])#вектор скорости


def init(): #задаем сетку, размерностью...
    ax.set_xlim([0., 10.])
    ax.set_ylim([0, 10.])
    return point,

h=0.05
g=-9.8
def updatefig(frame):
    #v[1] = v[1] + g*h
    coord[1] = coord[1] + v[1]*h #движение происходит по ОУ,  
    v[1] = v[1] + g*h
    if coord[1] > 10. or coord[1] < 0.: # если дошел до нижней или верхней границы
    	v[1] = -v[1]
    
#v[0] = v[0] + g*h
    coord[0] = coord[0] + v[0]*h #движение происходит по ОУ,  
    v[0] = v[0] + g*h
    if coord[0] > 10. or coord[0] < 0.: # если дошел до нижней или верхней границы
    	v[0] = -v[0]
    point.set_xdata(coord[0])
    point.set_ydata(coord[1])
    return point,

anim = animation.FuncAnimation(fig, updatefig, frames=2000000, init_func=init, interval=100, blit=True, repeat=False)

plt.show()



