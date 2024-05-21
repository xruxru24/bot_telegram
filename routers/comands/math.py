from sympy import solve, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
from time import time
import matplotlib.pyplot as plt
import numpy as np


class Math:

    def x(self, formula):
        start_time = time()
        transformations = (standard_transformations + (implicit_multiplication_application,))

        def map_operations(formula_str):
            return formula_str.replace("^", "**").replace("=", "-")

        f = parse_expr(map_operations(formula), transformations=transformations)
        roots = solve(f)
        end_time = time()

        return f'{roots} \nзатрачено времени {end_time - start_time}'

    def arithmetic(self, *args):
        return eval(*args)

    def func(self, x_and_y):
        x = ''
        i = 0
        while x_and_y[i] != ']':
            x += x_and_y[i]
            i += 1
        x += ']'
        y = x_and_y
        y = y.replace(x, '')
        x = eval(x)
        plt.style.use('_mpl-gallery')
        x0, x1, x2 = x
        x = np.linspace(x0, x1, x2)
        y = eval(''.join(y))
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2)
        fig.savefig('saved_figure.jpg')

