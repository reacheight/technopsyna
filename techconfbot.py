import re

from commands import bl, about_and_help, wolfram, tts, pidor, deer
from bot import bot

import config


@bot.message_handler(commands=['bl'])
def bl_command(message):
    bl.my_bl(message)


@bot.message_handler(commands=['wf', 'wolfram'])
def wf_command(message):
    wolfram.wolfram_command(message)


@bot.message_handler(commands=['tts', 'voice'])
def tts_command(message):
    tts.text_to_speech(message)


@bot.message_handler(commands=['deer_message'])
def deer_message_command(message):
    deer.get_messages(message)


@bot.message_handler(commands=['pidoreg'])
def pidoreg_command(message):
    pidor.registration(message)


@bot.message_handler(commands=['pidor'])
def pidor_command(message):
    pidor.choose_winner(message)


@bot.message_handler(commands=['help'])
def help_command(message):
    about_and_help.my_help(message)


@bot.message_handler(commands=['about', 'start'])
def about_command(message):
    about_and_help.about(message)


@bot.message_handler(commands=['kek'])
def kek(message):
    bot.send_message(message.chat.id, config.kek_message, reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['text'])
def bl_message(message):
    if 'ыыы' in message.text:
        bl.basic_bl(message)

    if re.search(config.chto_pacani_pattern, message.text):
        bot.send_sticker(message.chat.id, config.cho_pacani_anime_sticker, reply_to_message_id=message.message_id)

    if re.search(config.fuck_u_from_detur_pattern, message.text) and (message.from_user.username == 'MaliciousMoon' or
                                                  message.from_user.first_name == 'Detur'):
        bot.reply_to(message, config.fuck_u_detur)


@bot.inline_handler(func=lambda query: len(query.query.split()) > 1)
def query_text(query):
    com = query.query.split()[0]
    if com == 'wf':
        wolfram.wolfram_inline(query)

    elif com == 'voice' or com == 'tts':
        tts.text_to_speech_inline(query)


bot.skip_pending = True # чтобы можно было просто задеплоить
bot.polling(none_stop=True)
