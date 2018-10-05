import os
from random import choice, random, randint

import config
from bot import bot


def bl_string_message(message):
    probability = random()
    if probability <= 0.1:
        bot.reply_to(message, 'ы' * randint(5, 20))
    if probability >= 0.9:
        bot.send_message(message.chat.id, 'Прекратите!')


def bl_command(message):
    if message.chat.title == config.technoconfa_chatname and random() > 0.7:
        bot.send_message(message.chat.id, 'Не флудите.')
        return

    if random() <= 0.05:
        images = os.listdir(config.bl_images_locations)
        image_filename = choice(images)
        with open(config.bl_images_locations + image_filename, 'rb') as image:
            if image_filename.endswith('.gif'):
                bot.send_document(message.chat.id, image, reply_to_message_id=message.message_id)

            else:
                bot.send_photo(message.chat.id, image, reply_to_message_id=message.message_id)

    else:
        with open(config.bl_text_file, 'r', encoding='utf-8') as bl_file:
            bl_string = choice(list(bl_file)).rstrip()

            if bl_string.startswith('<sticker>'):
                sticker_id = bl_string[9:].strip()
                bot.send_sticker(message.chat.id, sticker_id, reply_to_message_id=message.message_id)

            else:
                bot.reply_to(message, bl_string.replace('<br>', '\n'))
