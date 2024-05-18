from aiogram import types
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

help_equations = 'help_quadratic_equations'


@router.message(Command("quadratic"))
async def start_quadratic(message: types.Message): # q = quadratic
    builder_start_quadratic = InlineKeyboardBuilder()
    builder_start_quadratic.add(types.InlineKeyboardButton(
        text="подсказка",
        callback_data=help_equations)
    )
    await message.answer(
        "напишите уравнение",
        reply_markup=builder_start_quadratic.as_markup()
    )


@router.callback_query(F.data == help_equations)
async def angly_callback_data_q_eq(callback: types.CallbackQuery):
    await callback.answer(
        text='''
1) бот решает квадратные уравнение где только 1 переменная не известна
2) бот решает только линейные уравнение''',
        show_alert=True
    )
