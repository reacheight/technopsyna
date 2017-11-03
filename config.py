import os

token = os.environ['BOT_TOKEN']

about_text_file = 'data/about_data/about_text_message'
help_text_file = 'data/help_data/help_text_message'
bl_text_file = 'data/bl_data/bl_text_messages'
bl_images_locations = 'data/bl_data/images/'

wolfram_appid = os.environ['WOLFRAM_APPID']
wolfram_bad_status_message = "Запрос не найдён.\nЕсли ты ввёл его на русском, то попробуй ввести его на английском."
wolfram_empty_query_message = "Использование: `/wolfram <запрос>` или `/wf <запрос>`"

tts_empty_query_message = "Использование: `/tts <запрос>` или `/wf <запрос>`"
