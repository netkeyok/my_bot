import openai
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.builtin import CommandStart
from openai import OpenAIError
import bot_config as config
from func import update


# настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

openai.api_key = config.gpt_key

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)

messages = [
    {
        "role": "system",
        "content": "You are a programming assistant, helping users with Python programming with popular frameworks."
    }
]

# Хэндлер на команду /start
@dp.message_handler(CommandStart())
async def start(message: types.Message):
    sender_id = message.from_user.id
    await message.answer("Привет, давай поболтаем с Chat-GPT")
    print(sender_id)

async def on_startup(dp):
    # Отправляем сообщение о том, что бот запущен
    await bot.send_message(chat_id=config.admin_id, text='Готов к труду!')




@dp.message_handler()
async def send(message: types.Message):
    try:
        update(messages, 'user', message.text)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        await message.answer(response['choices'][0]['message']['content'], parse_mode="markdown")
    except OpenAIError as ex:
        await message.answer(ex.error)


# Регистрируем обработчик on_startup
dp.register_event_handler(on_startup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
