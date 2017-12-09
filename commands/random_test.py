import config
from bot import bot

from random import choice


def get_random_test(subject):
    a = []

    with open(config.test_files[subject], "r") as f:
        a = f.readlines()

    return choice(a)


def random_test(message):
    subject = message.text.split()[1]
    bot.reply_to(message, get_random_test(subject))