from os import environ
from datetime import timedelta

redis_url = environ['REDIS_URL']
token = environ['BOT_TOKEN']
my_id = int(environ['MY_ID'])
wolfram_appid = environ['WOLFRAM_APPID']
wolfram_url = 'https://api.wolframalpha.com/v1/simple?appid=' + wolfram_appid
wolfram_max_ratio = 2.5
bl_text_file = 'static/bl_data/bl_text_messages'
bl_images_locations = 'static/bl_data/images/'
matan_image = 'static/matan.jpg'
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
    'about': 'static/about_command_text',
    'start': 'static/about_command_text',
    'help': 'static/help_command_text',
    'wiki': 'static/wiki_command_text',
    'internship': 'static/internship_command_text',
    'passing_scores': 'static/passing_scores',
    'olymp_privileges': 'static/olymp_privileges',
    'helpline': 'static/helpline'
}

ege_countdown_commands = {
    'math': ('2020-06-01', 'математике'),
    'rus': ('2020-05-28', 'русскому языку'),
    'inf': ('2020-05-25', 'информатике'),
    'phys': ('2020-06-04', 'физике')
}

larin_var_key = "latest_larin_var"
larin_variant_pdf_template = "https://alexlarin.net/ege/2020/trvar{}.pdf"
larin_check_time = timedelta(days=1)
