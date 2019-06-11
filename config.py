from os import environ
from datetime import timedelta

token = environ['BOT_TOKEN']
test_token = environ['TEST_BOT_TOKEN']
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
technoconfa_chatname = 'Техноконфа_2019'
bot_username = '@technoconfachbot'
logs_channel = '@technocofachbot_logs'
update_delete_user_time = timedelta(seconds=3600)
user_delete_time = timedelta(days=1)

text_commands = {
    'about': 'data/about_command_text',
    'start': 'data/about_command_text',
    'help': 'data/help_command_text',
    'wiki': 'data/wiki_command_text',
    'passing_scores': 'data/passing_scores',
    'olymp_privileges': 'data/olymp_privileges',
}
