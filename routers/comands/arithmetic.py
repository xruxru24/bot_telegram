from aiogram import types
from aiogram.types import CallbackQuery
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

help_arithmetic = 'help_arithmetic'


@router.message(Command("arithmetic"))
async def cmd_start(message: types.Message):
    await message.answer('arithmetic')
    builder_start_arithmetic = InlineKeyboardBuilder()
    builder_start_arithmetic.add(types.InlineKeyboardButton(
        text="подсказка",
        callback_data=help_arithmetic)
    )
    await message.answer(
        "напишите арфмитеческое действие",
        reply_markup=builder_start_arithmetic.as_markup()
    )


@router.callback_query(F.data == help_arithmetic)
async def angly_callback_data_arithmetic(callback_query: CallbackQuery):
    await callback_query.answer(
        text='''
1) бот умеет сравнивать примеры
2) складывать, умножать, делить, вычитание!!!
3) бот может работать с десятичными числами''',
        show_alert=True
    )


