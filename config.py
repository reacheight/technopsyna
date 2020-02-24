from os import environ
from datetime import timedelta

token = environ['BOT_TOKEN']
my_id = int(environ['MY_ID'])
wolfram_appid = environ['WOLFRAM_APPID']
wolfram_url = 'https://api.wolframalpha.com/v1/simple?appid=' + wolfram_appid
wolfram_max_ratio = 2.5
bl_text_file = 'data/bl_data/bl_text_messages'
bl_images_locations = 'data/bl_data/images/'
matan_image = 'data/matan.jpg'
new_member_sticker = 'CAADAgADrQEAAm29TQUoveU--qPBlAI'
cho_pacani_sticker = 'CAADAgADJwADtIuIDaIy4m-uZXREAg'
chto_pacani_pattern = r'(?iu).*чт?[оеё],? п[ао][цс][ао]ны'
deer_dembel_date = {'year': 2018, 'month': 12, 'day': 13}
technoconfa_chatname = 'Техноконфа_2020'
bot_username = '@technopsynabot'
logs_channel = '@technocofachbot_logs'
update_delete_user_time = timedelta(seconds=3600)
user_delete_time = timedelta(days=1)
dembel_message = '13 декабря 2018 года рядовой Олень с почётом закончил проходить военную службу ' \
                 'в рядах доблестной Росгвардии!'

text_commands = {
    'about': 'data/about_command_text',
    'start': 'data/about_command_text',
    'help': 'data/help_command_text',
    'wiki': 'data/wiki_command_text',
    'passing_scores': 'data/passing_scores',
    'olymp_privileges': 'data/olymp_privileges',
    'helpline': 'data/helpline'
}

ege_countdown_commands = {
    'math': ('2020-06-01', 'математике'),
    'rus': ('2020-05-28', 'русскому языку'),
    'inf': ('2020-05-25', 'информатике'),
    'phys': ('2020-06-04', 'физике')
}
