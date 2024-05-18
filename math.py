from sympy import solve, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
from main_bot import get_round_up
from time import time


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

print(x("x+200=300"))