from os import environ
from datetime import timedelta

redis_url = environ['REDIS_URL']
token = environ['BOT_TOKEN']
my_id = int(environ['MY_ID'])
wolfram_appid = environ['WOLFRAM_APPID']
wolfram_url = 'https://api.wolframalpha.com/v1/simple?appid=' + wolfram_appid
wolfram_max_ratio = 2.5
bl_text_file = 'technopsyna/static/bl_data/bl_text_messages'
bl_images_locations = 'technopsyna/static/bl_data/images/'
matan_image = 'technopsyna/static/matan.jpg'
vitek_voice = 'technopsyna/static/vitek.ogg'
new_member_sticker = 'CAADAgADrQEAAm29TQUoveU--qPBlAI'
cho_pacani_sticker = 'CAADAgADJwADtIuIDaIy4m-uZXREAg'
chto_pacani_pattern = r'(?iu).*чт?[оеё],? п[ао][цс][ао]ны'
deer_dembel_date = {'year': 2018, 'month': 12, 'day': 13}
technoconfa_chatname = 'Техноконфа_2021'
bot_username = '@technopsynabot'
update_delete_user_time = timedelta(seconds=3600)
user_delete_time = timedelta(days=1)
dembel_message = '13 декабря 2018 года рядовой Олень с почётом закончил проходить военную службу ' \
                 'в рядах доблестной Росгвардии!'

text_commands = ['about', 'help', 'helpline', 'internship', 'olymp_privileges', 'passing_scores', 'wiki']

ege_countdown_commands = {
    'math': ('2021-05-31', 'математике'),
    'rus': ('2021-05-27', 'русскому языку'),
    'inf': ('2021-06-18', 'информатике'),
    'phys': ('2021-06-03', 'физике')
}

larin_var_key = "latest_larin_var"
larin_variant_pdf_template = "https://alexlarin.net/ege/2021/trvar{}.pdf"
larin_check_time = timedelta(days=1)
