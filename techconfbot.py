import re

from commands import bl, about_and_help, wolfram, tts, deer, random_test, useful_links, number_fact, dembel_countdown
from bot import bot
from log import log

import config


@bot.message_handler(commands=['random_test'])
def random_test_command(message):
    random_test.random_test(message)
    log(message)


@bot.message_handler(commands=['bl'])
def bl_command(message):
    bl.my_bl(message)
    log(message)


@bot.message_handler(commands=['wf', 'wolfram'])
def wf_command(message):
    wolfram.wolfram_command(message)
    log(message)


@bot.message_handler(commands=['tts', 'voice'])
def tts_command(message):
    tts.text_to_speech(message)
    log(message)


@bot.message_handler(commands=['dembel'])
def dembel_command(message):
    dembel_countdown.dmb_days(message)
    log(message)


@bot.message_handler(commands=['number_fact'])
def number_fact_command(message):
    number_fact.type_number_fact(message)
    log(message)


@bot.message_handler(commands=['deer_message'])
def deer_message_command(message):
    deer.get_messages(message)
    log(message)


@bot.message_handler(commands=['help'])
def help_command(message):
    about_and_help.my_help(message)
    log(message)


@bot.message_handler(commands=['about', 'start'])
def about_command(message):
    about_and_help.about(message)
    log(message)

@bot.message_handler(commands=['links'])
def useful_links_command(message):
    useful_links.links(message)
    log(message)


@bot.message_handler(commands=['kek'])
def kek(message):
    bot.send_message(message.chat.id, config.kek_message, reply_to_message_id=message.message_id)
    log(message)


@bot.message_handler(content_types=['text'])
def bl_message(message):
    if 'ыыы' in message.text:
        bl.basic_bl(message)

    if re.search(config.chto_pacani_pattern, message.text):
        bot.send_sticker(message.chat.id, config.cho_pacani_anime_sticker, reply_to_message_id=message.message_id)

    log(message)


@bot.message_handler(content_types=['new_chat_members'])
def new_member_greeting(message):
    chatname = message.chat.title
    username = message.new_chat_members[0].username

    if chatname == config.technoconfa:
        if username:
            bot.send_message(message.chat.id, '@' + username)

        bot.send_sticker(message.chat.id, config.chto_sdaesh_sticker)


@bot.inline_handler(func=lambda query: len(query.query.split()) > 1)
def query_text(query):
    com = query.query.split()[0]
    if com == 'wf':
        wolfram.wolfram_inline(query)

    elif com == 'voice' or com == 'tts':
        tts.text_to_speech_inline(query)


bot.polling(none_stop=True)
