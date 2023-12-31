import openai
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.builtin import CommandStart
from openai import OpenAIError
import bot_config as config



# настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

openai.api_key = config.gpt_key

bot = Bot(token=config.bot_token, parse_mode="Markdown")
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

def update(messages, role, content):
    """
    Функция обновления списка сообщений
    """
    messages.append({"role": role, "content": content})


@dp.message_handler()
async def send(message: types.Message):
    try:
        update(messages, 'user', message.text)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )
        await message.answer(response['choices'][0]['message']['content'])
    except OpenAIError as ex:
        await message.answer(ex.error)


async def on_startup(dp: Dispatcher):
    for user_id in config.admin_id:
        await bot.send_message(user_id, "Привет! Я снова в сети и готов помогать вам с программированием на Python.")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
