import re
import config

from commands import bl, wolfram, dembel_countdown
from bot import bot
from logger import log


@bot.message_handler(commands=['start', 'about', 'help', 'passing_scores', 'wiki', 'olymp_privileges'])
def text_commands(message):
    log(message)
    command = message.text.split(maxsplit=1)[0][1:]
    if command.lower().endswith(config.bot_username):
        command = command[:-17]

    if command in config.text_command_file.keys():
        with open(config.text_command_file[command], 'r') as file:
            bot.send_message(message.chat.id, file.read().strip(), parse_mode='Markdown',
                             disable_web_page_preview=True)


@bot.message_handler(commands=['bl'])
def bl_command(message):
    log(message)
    bl.bl_command(message)


@bot.message_handler(commands=['wf'])
def wf_command(message):
    log(message)
    wolfram.wolfram_command(message)


@bot.message_handler(commands=['dembel'])
def dembel_command(message):
    log(message)
    dembel_countdown.dembel_command(message)


@bot.message_handler(content_types=['text'])
def bl_message(message):
    if 'ыыы' in message.text:
        bl.bl_string(message)

    if re.search(config.chto_pacani_pattern, message.text):
        bot.send_sticker(message.chat.id, config.cho_pacani_anime_sticker, reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['new_chat_members'])
def new_member_greeting(message):
    chatname = message.chat.title
    user = message.new_chat_members[0]
    username = '@' + user.username if user.username else user.first_name

    if chatname == config.technoconfa_chatname:
        bot.send_message(message.chat.id, 'Привет, ' + username + '!')
        bot.send_sticker(message.chat.id, config.new_member_sticker)


@bot.inline_handler(func=lambda query: len(query.query.split()) > 1 and query.query.split()[0] == 'wf')
def inline_query(query):
    wolfram.wolfram_inline(query)


bot.polling(none_stop=True)
