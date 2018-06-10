import os
from random import choice, randint

import config
from bot import bot


def bl_string(message):
    random_integer = randint(1, 100)
    if random_integer in range(1, 10):
        bot.reply_to(message, 'ы' * randint(5, 20))
    if random_integer in range(30, 35):
        bot.send_message(message.chat.id, 'Прекратите!')


def bl_command(message):
    if message.chat.title == config.technoconfa and randint(1, 10) > 7:
        bot.send_message(message.chat.id, 'Не флудите.')
        return

    if randint(1, 33) == 22:
        images = os.listdir(config.bl_images_locations)
        image_filename = choice(images)
        with open(config.bl_images_locations + image_filename, 'rb') as image:
            if image_filename.endswith('.gif'):
                bot.send_document(message.chat.id, image, reply_to_message_id=message.message_id)

            else:
                bot.send_photo(message.chat.id, image, reply_to_message_id=message.message_id)

    else:
        with open(config.bl_text_file, 'r', encoding='utf-8') as bl_file:
            bl = choice(bl_file.readlines())

            if str(bl).startswith('<sticker>'):
                sticker_id = str(bl[9:]).strip()
                bot.send_sticker(message.chat.id, sticker_id, reply_to_message_id=message.message_id)

            else:
                bot.reply_to(message, str(bl).replace('<br>', '\n'))
