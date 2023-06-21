import openai
import bot_config as config


openai.api_key = config.gpt_key


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
