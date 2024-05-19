from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command
from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from states import FunctionsDialog
from routers.comands.math import Math


router = Router()

help_equations = 'help_quadratic_equations'
bot = Bot(token="7025395033:AAFiyenAhKRk3K1aoPmB90vOZFkuQ37CLE0")


@router.message(Command("quadratic"))
async def start_quadratic(message: types.Message, state: FSMContext):
    builder_start_quadratic = InlineKeyboardBuilder()
    builder_start_quadratic.add(types.InlineKeyboardButton(
        text="подсказка",
        callback_data=help_equations)
    )
    await bot.send_message(message.from_user.id,
                           text='введите уравнение',
                           reply_markup=builder_start_quadratic.as_markup()
                           )

    await state.set_state(FunctionsDialog.functions_save)


@router.message(FunctionsDialog.functions_save)
async def quadratic_save(message: types.Message, state: FSMContext):
    quadratic_text = message.text
    solved_equation = Math()
    await bot.send_message(message.from_user.id, text=f'{solved_equation.x(quadratic_text)}')
    await state.clear()


@router.callback_query(F.data == help_equations)
async def angly_callback_data_q_eq(callback: types.CallbackQuery):
    await callback.answer(
        text='бот решает только линейные уравнение',
        show_alert=True
    )
