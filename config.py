import os

token = os.environ['BOT_TOKEN']
my_id = int(os.environ['MY_ID'])

text_command_file = {
    'about': 'data/about_data/about_text_message',
    'start': 'data/about_data/about_text_message',
    'help': 'data/help_data/help_text_message',
    'links': 'data/links_list',
    'passing_scores': 'data/passing_scores'
}

bl_text_file = 'data/bl_data/bl_text_messages'
bl_images_locations = 'data/bl_data/images/'

wolfram_appid = os.environ['WOLFRAM_APPID']
wolfram_url = "https://api.wolframalpha.com/v1/simple?appid=" + wolfram_appid
wolfram_bad_status_message = "Запрос не найдён.\nЕсли ты ввёл его на русском, то попробуй ввести его на английском."
wolfram_empty_query_message = "Использование: `/wolfram <запрос>` или `/wf <запрос>`"


chto_sdaesh_sticker = 'CAADAgADrQEAAm29TQUoveU--qPBlAI'
cho_pacani_anime_sticker = 'CAADAgADJwADtIuIDaIy4m-uZXREAg'
chto_pacani_pattern = r'(?iu).*чт?[оеё],? п[ао][цс][ао]ны'
integer_pattern = r'[\d]+'

deer_dembel_date = {'year': 2018, 'month': 12, 'day': 13}

technoconfa = 'Техноконфа_2018'
