import config
from bot import bot


def bot_command_help(message):
    help_message = open(config.help_text_file, 'r', encoding='utf-8')
    bot.reply_to(message, help_message.read().strip())
    help_message.close()
