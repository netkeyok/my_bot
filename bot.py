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


def update(messages, role, content):
    """
    Функция обновления списка сообщений
    """
    messages.append({"role": role, "content": content})


def reset_messages():
    """
    Функция очистки истории сообщений контекста, чтобы избежать ошибки с токенами
    """
    messages.clear()
    messages.append({
        "role": "system",
        "content": "You are a programming assistant, helping users with Python programming with popular frameworks."
    })


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
