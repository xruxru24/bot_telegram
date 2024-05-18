import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from routers import router as main_router
import button as button


logging.basicConfig(level=logging.INFO)


bot = Bot(token="7025395033:AAFiyenAhKRk3K1aoPmB90vOZFkuQ37CLE0")
dp = Dispatcher()
dp.include_router(main_router)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет, этот математический бот. Для подробной информации напишите /help")


@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer('''Этот бот умееет
                        1) решать арифметические операции по команде /arithmetic
                        2) решение линейных уравнений /quadratic
                        3) решать графики функций /functions
                        4) выбрать до кого числа будет округляться числа /round_up ()''')


@dp.message(Command("round_up"))
async def round_the_number(message: types.Message):
    global round_up
    round_up = 3
    await message.answer('напишите до какого числа будут округляться ответы')


def get_round_up():
    return round_up


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


