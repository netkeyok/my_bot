import openai
import bot_config as config


openai.api_key = config.gpt_key


def inputgpt(content):
    messages = [{"role": "system", "content": "Ты сеньер Fullstack, python разработчик"},
                {"role": "user", "content": content}]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    chat_response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_response})
    return chat_response
