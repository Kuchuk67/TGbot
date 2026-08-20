import asyncio
import logging
import os

# Bot —объект для работы с Telegram Bot API.
# Dispatcher — центральный диспетчер событий. Он получает update от Telegram и решает, какой обработчик должен его обработать.
from aiogram import Bot, Dispatcher 
# CommandStart — готовый фильтр для команды /start.
from aiogram.filters import CommandStart
# Message — тип объекта входящего Telegram-сообщения.
from aiogram.types import Message
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer("Бот работает.")


@dp.message()
async def echo(message: Message) -> None:
    if message.text:
        await message.answer(f"Вы написали: {message.text}")


async def main() -> None:
    token = os.environ.get("BOT_TOKEN")

    if not token:
        raise RuntimeError("BOT_TOKEN is not set")

    bot = Bot(token=token)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())