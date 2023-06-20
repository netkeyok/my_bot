import openai
from bot_config import config


openai.api_key = config.gpt_key.get_secret_value()


def inputgpt(content):
    messages = [{"role": "system", "content": "Ты сеньер Fullstack, python разработчик"},
                {"role": "user", "content": content}]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    chat_response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_response})
    return chat_response
