import os


bot_token = os.getenv('BOT_TOKEN')
gpt_key = os.getenv('GPT_KEY')
admin_id = ('460379779',)
max_tokens = '4096'
usage_check_frequency = '100'

# class Settings(BaseSettings):
#     # Желательно вместо str использовать SecretStr
#     # для конфиденциальных данных, например, токена бота
#     bot_token: SecretStr
#     gpt_key: SecretStr

#     # Вложенный класс с дополнительными указаниями для настроек
#     class Config:
#         # Имя файла, откуда будут прочитаны данные
#         # (относительно текущей рабочей директории)
#         env_file = env_path
#         # Кодировка читаемого файла
#         env_file_encoding = 'utf-8'


# # При импорте файла сразу создастся
# # и провалидируется объект конфига,
# # который можно далее импортировать из разных мест
# config = Settings()
