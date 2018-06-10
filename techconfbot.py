import re

from commands import bl, about_and_help, wolfram, useful_links, dembel_countdown, passing_scores
from bot import bot

import config


@bot.message_handler(commands=['passing_scores'])
def passing_scores_command(message):
    passing_scores.passing_scores(message)


@bot.message_handler(commands=['bl'])
def bl_command(message):
    bl.my_bl(message)


@bot.message_handler(commands=['wf', 'wolfram'])
def wf_command(message):
    wolfram.wolfram_command(message)


@bot.message_handler(commands=['dembel'])
def dembel_command(message):
    dembel_countdown.dmb_days(message)


@bot.message_handler(commands=['help'])
def help_command(message):
    about_and_help.my_help(message)


@bot.message_handler(commands=['about', 'start'])
def about_command(message):
    about_and_help.about(message)


@bot.message_handler(commands=['links'])
def useful_links_command(message):
    useful_links.links(message)


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


bot.polling(none_stop=True)
