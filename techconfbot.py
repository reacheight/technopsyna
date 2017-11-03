from commands import bl, about_and_help, wolfram, tts, pidor
from bot import bot


@bot.message_handler(commands=['bl'])
def bl_command(message):
    bl.my_bl(message)


@bot.message_handler(commands=['wf', 'wolfram'])
def wf_command(message):
    wolfram.wolfram_solver(message)


@bot.message_handler(commands=['tts', 'voice'])
def tts_command(message):
    tts.text_to_speech(message)


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


@bot.message_handler(content_types=['text'])
def bl_message(message):
    if 'ыыы' in message.text:
        bl.basic_bl(message)


bot.polling(none_stop=True)
