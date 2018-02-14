import re

from commands import bl, about_and_help, wolfram, tts, deer, random_test, useful_links, number_fact, dembel_countdown,\
    excuse_generator
from bot import bot

import config


@bot.message_handler(commands=['random_test'])
def random_test_command(message):
    random_test.random_test(message)


@bot.message_handler(commands=['bl'])
def bl_command(message):
    bl.my_bl(message)


@bot.message_handler(commands=['wf', 'wolfram'])
def wf_command(message):
    wolfram.wolfram_command(message)


@bot.message_handler(commands=['tts', 'voice'])
def tts_command(message):
    tts.text_to_speech(message)


@bot.message_handler(commands=['dembel'])
def dembel_command(message):
    dembel_countdown.dmb_days(message)


@bot.message_handler(commands=['excuse'])
def excuse_command(message):
    excuse_generator.send_excuse(message)


@bot.message_handler(commands=['number_fact'])
def number_fact_command(message):
    number_fact.type_number_fact(message)


@bot.message_handler(commands=['deer_message'])
def deer_message_command(message):
    deer.get_messages(message)


@bot.message_handler(commands=['help'])
def help_command(message):
    about_and_help.my_help(message)


@bot.message_handler(commands=['about', 'start'])
def about_command(message):
    about_and_help.about(message)

@bot.message_handler(commands=['links'])
def useful_links_command(message):
    useful_links.links(message)


@bot.message_handler(commands=['kek'])
def kek(message):
    bot.send_message(message.chat.id, config.kek_message, reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['text'])
def bl_message(message):
    if 'ыыы' in message.text:
        bl.basic_bl(message)

    if re.search(config.chto_pacani_pattern, message.text):
        bot.send_sticker(message.chat.id, config.cho_pacani_anime_sticker, reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['new_chat_members'])
def new_member_greeting(message):
    chatname = message.chat.title
    user = message.new_chat_members[0]
    username = '@' + user.username if user.username else user.first_name

    if chatname == config.technoconfa:
        bot.send_message(message.chat.id, 'Привет, ' + username + '!')
        bot.send_sticker(message.chat.id, config.chto_sdaesh_sticker)


@bot.inline_handler(func=lambda query: len(query.query.split()) > 1)
def query_text(query):
    com = query.query.split()[0]
    if com == 'wf':
        wolfram.wolfram_inline(query)

    elif com == 'voice' or com == 'tts':
        tts.text_to_speech_inline(query)


bot.polling(none_stop=True)
