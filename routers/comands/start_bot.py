import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from routers import router as main_router


logging.basicConfig(level=logging.INFO)

round_up = 3
bot = Bot(token="7025395033:AAFiyenAhKRk3K1aoPmB90vOZFkuQ37CLE0")
dp = Dispatcher()
dp.include_router(main_router)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет, этот математический бот. Для подробной информации напишите📋: /help")


@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer('''Этот бот умееет🤖:
1) решать арифметические операции по команде📟: \n/arithmetic
2) решение линейных уравнений по команде📖: \n /quadratic
3) решать графики функций по команде📈: \n /functions''')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


