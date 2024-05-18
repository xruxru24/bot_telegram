from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


MAIN_MENU = ReplyKeyboardBuilder()
MAIN_MENU.row(
        types.KeyboardButton(text="квадратные уравнения"),
    )
MAIN_MENU.row(
    types.KeyboardButton(text="Корни"),
    )
MAIN_MENU.row(
        types.KeyboardButton(text="арифметические операции"),
    )

