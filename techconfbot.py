from commands import bl, help
from bot import bot


@bot.message_handler(commands=['bl'])
def bl_command(message):
    bl.my_bl(message)


@bot.message_handler(commands=['help'])
def help_command(message):
    help.bot_command_help(message)


@bot.message_handler(content_types=['text'])
def bl_message(message):
    if 'ыыы' in message.text:
        bl.basic_bl(message)


bot.polling(none_stop=True)
