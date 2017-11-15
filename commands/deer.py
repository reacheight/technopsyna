from bot import bot
import config

from random import choice


def get_messages(message):
    deer_messages = open(config.deer_messages_location, 'r')
    text = choice(deer_messages.readlines())
    deer_messages.close()
    bot.reply_to(message, text)