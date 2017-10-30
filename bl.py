from bot import bot
from random import choice, randint

import config


def basic_bl(message):
    bot.reply_to(message, 'ы' * randint(5, 20))


def my_bl(message):
    bl_file = open(config.bl_location, 'r', encoding='utf-8')
    your_bl = choice(bl_file.readlines())

    if str(your_bl).startswith("<sticker>"):
        sticker_id = your_bl[9:]
        bot.send_sticker(message.chat.id, sticker_id, reply_to_message_id=message.message_id)

    else:
        bot.reply_to(message, str(your_bl))

    bl_file.close()

