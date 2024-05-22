from aiogram.filters.state import StatesGroup, State


class QuadraticDialog(StatesGroup):
    quadratic_solution = State()


class FunctionsDialog(StatesGroup):
    functions_save_solution = State()


class ArithmeticDialog(StatesGroup):
    arithmetic_solution = State()
