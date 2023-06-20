import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from bot_config import config
from func import inputgpt


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    sender_id = message.from_user.id
    await message.answer("Привет, давай поболтаем с Chat-GPT")
    print(sender_id)


# Обработка сообщений
@dp.message()
async def echo(message: types.Message):
    # передаем сообщение в функцию inputChat и получаем результат
    result = inputgpt(message.text)
    # отвечаем на сообщение результатом работы функции
    await message.answer(result)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
