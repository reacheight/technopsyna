import os

token = os.environ['BOT_TOKEN']

about_text_file = 'data/about_data/about_text_message'
help_text_file = 'data/help_data/help_text_message'
bl_text_file = 'data/bl_data/bl_text_messages'
bl_images_locations = 'data/bl_data/images/'
links_list = 'data/links_list'
passing_scores_file = 'data/passing_scores'

wolfram_appid = os.environ['WOLFRAM_APPID']
wolfram_bad_status_message = "Запрос не найдён.\nЕсли ты ввёл его на русском, то попробуй ввести его на английском."
wolfram_empty_query_message = "Использование: `/wolfram <запрос>` или `/wf <запрос>`"

my_id = os.environ['MY_ID']

chto_sdaesh_sticker = 'CAADAgADrQEAAm29TQUoveU--qPBlAI'
cho_pacani_anime_sticker = 'CAADAgADJwADtIuIDaIy4m-uZXREAg'
chto_pacani_pattern = r'(?iu).*чт?[оеё],? п[ао][цс][ао]ны'
integer_pattern = r'[\d]+'

deer_dembel_date = {'year' : 2018, 'month' : 12, 'day' : 13}

technoconfa = 'Техноконфа_2018'
