from bot import bot

import config
from bl import my_bl, basic_bl


@bot.message_handler(commands=['bl'])
def bl_command(message):
    my_bl(message)


@bot.message_handler(content_types=['text'])
def bl_message(message):
    if 'ыыы' in message.text:
        basic_bl(message)


bot.polling(none_stop=True)
