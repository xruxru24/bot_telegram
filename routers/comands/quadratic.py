from aiogram import types
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram import F, Router
from aiogram.filters import Command


router = Router()

help_quadratic_equations = 'help_quadratic_equations'


@router.message(Command("quadratic"))
async def cmd_start(message: types.Message):
    await message.answer('quadratic')
    complete_q_eq = InlineKeyboardButton(text='подсказка',
                                         callback_data=help_quadratic_equations,
                                         )


@router.callback_query(F.data == help_quadratic_equations)
async def angly_callback_data_q_eq(callback_query: CallbackQuery):
    await callback_query.answer(
        text='''бот умеет решать только линейные уравнение!!!''',
        show_alert=True
    )


