from aiogram import F, Router
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command
from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.media_group import MediaGroupBuilder
from states import FunctionsDialog
from routers.comands.math import Math
from time import time


router = Router()

help_functions = 'help_functions'
help_functions_two = 'help_functions_two'
bot = Bot(token="7025395033:AAFiyenAhKRk3K1aoPmB90vOZFkuQ37CLE0")


@router.message(Command("functions"))
async def start_functions(message: types.Message, state: FSMContext):
    builder_start_functions = InlineKeyboardBuilder()
    builder_start_functions.add(types.InlineKeyboardButton(
        text="подсказка",
        callback_data=help_functions),
        types.InlineKeyboardButton(
        text="подсказка 2",
        callback_data=help_functions_two)
    )
    await bot.send_message(message.from_user.id,
                           text='введите график функции',
                           reply_markup=builder_start_functions.as_markup()
                           )

    await state.set_state(FunctionsDialog.functions_save_solution)


@router.message(FunctionsDialog.functions_save_solution)
async def functions_save(message: types.Message, state: FSMContext):
    try:
        start_time = time()
        functions_text = message.text
        functions_res = Math()
        album_builder = MediaGroupBuilder(
            caption=f'готовый график: \n { functions_res.func(functions_text)} \nпотрачено время: {time() - start_time}'
        )
        album_builder.add(
            type="photo",
            media=FSInputFile("saved_figure.jpg")
        )
        await message.answer_media_group(
            media=album_builder.build()
        )
        await state.clear()
    except IndexError:
        await message.answer('Ошибка ввода, введите ещё раз')
    except ZeroDivisionError:
        await message.answer('Ошибка в функции, введите ещё раз')


@router.callback_query(F.data == help_functions)
async def angly_callback_data_functions(callback: types.CallbackQuery):
    await callback.answer(
        text='оформление: синус - np.cos(x), косинус - np.sin(x), Тангенс -np.tan(x),	Арккосинус - np.acos, Арксинус - np.asin, Арктангенс - np.atan(x), Экспонента - np.exp, Логарифм - np.log',
        show_alert=True
    )


@router.callback_query(F.data == help_functions_two)
async def angly_callback_data_functions_two(callback: types.CallbackQuery):
    await callback.answer(
        text='корень - sqrt(x) степень - x ** 2. Оформление графика функций выглядит так 1) введите три значение  в квадратные скобки x ЧЕРЕЗ ЗАПЯТУЮ 2) чему равен y пример: [1, 10, 100] x + 4',
        show_alert=True
    )

