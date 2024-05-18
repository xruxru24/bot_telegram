from sympy import solve, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

formula = "x+226=300"

def map_operations(formula_str):
    return formula_str.replace("^", "**").replace("=", "-")

f = parse_expr(map_operations(formula), transformations=transformations)
roots = solve(f)
print(*roots)