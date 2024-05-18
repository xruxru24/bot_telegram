from sympy import solve, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
from time import time
import matplotlib.pyplot as plt
import numpy as np

transformations = (standard_transformations + (implicit_multiplication_application,))


def x(formula):
    start_time = time()

    def map_operations(formula_str):
        return formula_str.replace("^", "**").replace("=", "-")

    f = parse_expr(map_operations(formula), transformations=transformations)
    roots = solve(f)
    end_time = time()

    return f'{roots} затрачено времени {end_time - start_time}'


def arithmetic(*args):
    try:
        return eval(*args)
    except:
        return 'Ошибка ввода'


def func(x_list, y_func):
    plt.style.use('_mpl-gallery')
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

func([], 'np.sin(x)')
