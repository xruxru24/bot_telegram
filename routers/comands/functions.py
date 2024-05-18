from aiogram import types
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

help_functions = 'help_functions'


@router.message(Command("functions"))
async def start_functions(message: types.Message):
    builder_start_functions = InlineKeyboardBuilder()
    builder_start_functions.add(types.InlineKeyboardButton(
        text="подсказка",
        callback_data=help_functions)
    )
    await message.answer(
        "напишите уравнение",
        reply_markup=builder_start_functions.as_markup()
    )


@router.callback_query(F.data == help_functions)
async def angly_functions(callback: types.CallbackQuery):
    await callback.answer(
        text='''
1) введите 3 точки x, если вы введите больше или меньше трех точек, то сработает значение по умолчанию (0, 10, 100)
2) оформление выглядит так: синус - np.cos(x), косинус - np.sin(x), Тангенс -np.tan(x),	Арккосинус - np.acos, Арксинус - np.asin,
Арктангенс - np.atan(x), Экспонента - np.exp, Логарифм - np.log	
''',
        show_alert=True
    )
