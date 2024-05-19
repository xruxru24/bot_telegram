from aiogram.filters.state import StatesGroup, State


class QuadraticDialog(StatesGroup):
    quadratic_save = State()


class FunctionsDialog(StatesGroup):
    functions_save = State()


class ArithmeticDialog(StatesGroup):
    arithmetic_save = State()
