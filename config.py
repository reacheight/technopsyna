import os

token = os.environ['BOT_TOKEN']

about_text_file = 'data/about_data/about_text_message'
help_text_file = 'data/help_data/help_text_message'
bl_text_file = 'data/bl_data/bl_text_messages'
bl_images_locations = 'data/bl_data/images/'

wolfram_appid = os.environ['WOLFRAM_APPID']
wolfram_bad_status_message = "Запрос не найдён.\nЕсли ты ввёл его на русском, то попробуй ввести его на английском."
wolfram_empty_query_message = "Использование: `/wolfram <запрос>` или `/wf <запрос>`"

tts_empty_query_message = "Использование: `/voice <запрос>` или `/tts <запрос>`"

pidor_already_registred_message = "Ты уже зарегистрирован в игре!"
pidor_noone_registred_message = "В игре нет зарегистрированных!"
pidor_now_registred = "Теперь ты учавствуешь в розыгрыше!"
pidor_one_registred_message = "Пока только один человек зарегистрировался в игре! Нужно как минимум два!"
pidor_recognized = "Пидоря дня — @"
pidor_registred = []
pidor_text_files = 'data/pidor_data/text_files/'
pidor_audio_files = 'data/pidor_data/audio_files/'

my_id = os.environ['MY_ID']

kek_message = "Вы ботом ошиблись.."

cho_pacani_anime_sticker = 'CAADAgADFwADWmd_DLq2Y8q2ciHRAg'