from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from routers.comands.math import Math
from states import ArithmeticDialog
from time import time
from math import ceil


router = Router()

help_arithmetic = 'help_arithmetic'
bot = Bot(token="7025395033:AAFiyenAhKRk3K1aoPmB90vOZFkuQ37CLE0")


@router.message(Command("arithmetic"))
async def start_quadratic(message: types.Message, state: FSMContext):
    builder_start_help_arithmetic = InlineKeyboardBuilder()
    builder_start_help_arithmetic.add(types.InlineKeyboardButton(
        text="подсказка",
        callback_data=help_arithmetic)
    )
    await bot.send_message(message.from_user.id,
                           text='введите пример',
                           reply_markup=builder_start_help_arithmetic.as_markup()
                           )

    await state.set_state(ArithmeticDialog.arithmetic_save)


@router.message(ArithmeticDialog.arithmetic_save)
async def quadratic_save(message: types.Message, state: FSMContext):
    try:
        start_time = time()
        arithmetic_text = message.text
        arithmetic_equation = Math()
        await bot.send_message(message.from_user.id, text=f'{arithmetic_equation.arithmetic(arithmetic_text)} \nпотрачено время: {time() - start_time}')
        await state.clear()
    except NameError:
        await message.answer('ошибка ввода, введите ещё раз')


@router.callback_query(F.data == help_arithmetic)
async def angly_callback_data_arithmetic(callback_query: CallbackQuery):
    await callback_query.answer(
        text='1) бот умеет сравнивать примеры 2) складывать, умножать, делить, вычитание!!! 3) бот может работать с десятичными числами',
        show_alert=True
    )


