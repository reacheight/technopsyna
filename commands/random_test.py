import config
from bot import bot

from random import choice


def get_random_test(subject):
    a = []
    with open(config.test_files[subject], "r") as f:
        a = f.readlines()

    return choice(a)


def random_test(message):
    splited = message.text.split()
    if len(splited) < 2 or splited[1] not in config.test_files:
        bot.reply_to(message, config.random_test_error_subject, parse_mode='Markdown')
        return

    bot.reply_to(message, get_random_test(splited[1]), disable_web_page_preview=True)