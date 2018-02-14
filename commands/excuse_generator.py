import config
from bot import bot
from random import randint, choice


def generate_excuse(object):
    if randint(1, 10) > 5:
        with open(config.pre_excuses, 'r') as f:
            excuse = choice(f.readlines()).lstrip() + ' ' + object

    else:
        with open(config.post_excuses, 'r') as f:
            excuse = object + choice(f.readlines())

    return excuse


def send_excuse(message):
    splited = message.text.split(maxsplit=1)
    if len(splited) < 2:
        bot.reply_to(message, config.excuse_empty_message, parse_mode="Markdown")
        return

    bot.reply_to(message, generate_excuse(splited[1]))
