import re
import config

from bot import bot
from commands import bl, wolfram, dembel_countdown
from logger import log


@bot.message_handler(commands=list(config.text_commands.keys()))
def text_commands(message):
    log(message)
    command = message.text.split('@', 1)[0][1:]

    with open(config.text_commands[command], 'r') as file:
        bot.send_message(message.chat.id, file.read().strip(), parse_mode='Markdown',
                         disable_web_page_preview=True)


@bot.message_handler(commands=['bl'])
def bl_command(message):
    log(message)
    bl.bl_command(message)


@bot.message_handler(commands=['matan'])
def matan_command(message):
    log(message)
    if message.from_user.id == config.my_id:
        with open(config.matan_image, 'rb') as image:
            bot.send_photo(message.chat.id, image)


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
        bl.bl_string_message(message)

    if re.search(config.chto_pacani_pattern, message.text):
        bot.send_sticker(message.chat.id, config.cho_pacani_sticker, reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['new_chat_members'])
def new_member_greeting(message):
    chat_name = message.chat.title

    if chat_name != config.technoconfa_chatname:
        return

    user = message.new_chat_members[0]
    username = '@' + user.username if user.username else user.first_name

    bot.send_message(message.chat.id, f'Привет, {username}! Представься, пожалуйста.')
    bot.send_sticker(message.chat.id, config.new_member_sticker)


@bot.inline_handler(func=lambda query: len(query.query.split()) > 1 and query.query.split()[0] == 'wf')
def inline_query(query):
    wolfram.wolfram_inline(query)


bot.polling(none_stop=True)
