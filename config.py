import os

token = os.environ['BOT_TOKEN']
my_id = int(os.environ['MY_ID'])

text_command_file = {
    'about': 'data/about_command_text',
    'start': 'data/about_command_text',
    'help': 'data/help_command_text',
    'wiki': 'data/wiki_command_text',
    'passing_scores': 'data/passing_scores',
    'olymp_privileges': 'data/olymp_privileges'
}

bl_text_file = 'data/bl_data/bl_text_messages'
bl_images_locations = 'data/bl_data/images/'

wolfram_appid = os.environ['WOLFRAM_APPID']
wolfram_url = "https://api.wolframalpha.com/v1/simple?appid=" + wolfram_appid
wolfram_bad_status_message = "Запрос не найдён.\nЕсли ты ввёл его на русском, то попробуй ввести его на английском."
wolfram_empty_query_message = "Использование: `/wf <запрос>`"

new_member_sticker = 'CAADAgADrQEAAm29TQUoveU--qPBlAI'
cho_pacani_anime_sticker = 'CAADAgADJwADtIuIDaIy4m-uZXREAg'
chto_pacani_pattern = r'(?iu).*чт?[оеё],? п[ао][цс][ао]ны'

deer_dembel_date = {'year': 2018, 'month': 12, 'day': 13}

technoconfa_chatname = 'Техноконфа_2019'
bot_username = '@technoconfachbot'

logs_channel = '@technocofachbot_logs'

matan_image = 'data/matan.jpg'
