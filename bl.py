import os
from bot import bot
from random import choice, randint

import config


def basic_bl(message):
    rand = randint(1, 100)
    if rand in range(1, 30):
        bot.reply_to(message, 'ы' * randint(5, 20))
    if rand in range(31, 40):
        bot.send_message(message.chat.id, "Прекратите!")


def my_bl(message):
    if randint(1, 100) in range(1, 20):
        imgs = os.listdir(config.bl_images_locations)
        random_file = choice(imgs)
        your_img = open(config.bl_images_locations + random_file, "rb")

        if random_file.endswith(".gif"):
            bot.send_document(message.chat.id, your_img, reply_to_message_id=message.message_id)

        else:
            bot.send_photo(message.chat.id, your_img, reply_to_message_id=message.message_id)

        your_img.close()

    else:
        bl_file = open(config.bl_text_file, 'r', encoding='utf-8')
        your_bl = choice(bl_file.readlines())

        if str(your_bl).startswith("<sticker>"):
            if randint(1, 100) in range(1, 70):
                sticker_id = str(your_bl[9:]).strip()
                bot.send_sticker(message.chat.id, sticker_id, reply_to_message_id=message.message_id)
            else:
                bot.send_message(message.chat.id, "Хватит ыкать!")

        else:
            bot.reply_to(message, str(your_bl))

        bl_file.close()

