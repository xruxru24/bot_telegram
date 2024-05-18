import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')


def func(x_list, y_func):
    try:
        if len(x_list) != 2:
            x0, x1, x2 = 0, 10, 100
        else:
            x0, x1, x2 = x_list
        x = np.linspace(x0, x1, x2)
        y = eval(y_func)
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)
    except:
        print('ошибка ввода')

    plt.show()


func([], 'x + 4')



x = np.linspace(0, 20, 100)