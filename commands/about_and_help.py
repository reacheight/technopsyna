import config
from bot import bot


def my_help(message):
    help_message = open(config.help_text_file, 'r', encoding='utf-8')
    bot.send_message(message.chat.id, help_message.read().strip(), parse_mode="Markdown", disable_webpage_preview=True)

    help_message.close()


def about(message):
    about_message = open(config.about_text_file, 'r', encoding='utf-8')
    bot.reply_to(message, about_message.read().strip(), parse_mode="Markdown")

    about_message.close()
