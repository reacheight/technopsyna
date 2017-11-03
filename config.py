import os

token = os.environ['BOT_TOKEN']

bl_text_file = 'data/bl_data/bl_text_messages'
help_text_file = 'data/help_data/help_text_message'
bl_images_locations = 'data/bl_data/images/'

wolfram_appid = os.environ['WOLFRAM_APPID']
wolfram_bad_status_message = "Запрос не найдён.\nЕсли ты ввёл его на русском, то попробуй ввести его на английском."
wolfram_empty_query_message = "Использование: `/wolfram <запрос>` или `/wf <запрос>`"
