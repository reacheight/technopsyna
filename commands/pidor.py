import time
import os
from random import choice, randint

import config
from bot import bot


def registration(message):
    if message.from_user.id not in config.pidor_registred:
        config.pidor_registred.append(message.from_user)
        bot.reply_to(message, config.pidor_now_registred)

    else:
        bot.reply_to(message, config.pidor_already_registred_message)


def choose_winner(message):
    if len(config.pidor_registred) == 0:
        bot.reply_to(message, config.pidor_noone_registred_message)

    elif len(config.pidor_registred) == 1:
        bot.reply_to(message, config.pidor_one_registred_message)

    else:
        pidor_username = choice(config.pidor_registred).username

        if randint(1, 100) in range(1, 20):
            audio_files = os.listdir(config.pidor_audio_files)
            random_audio_file = choice(audio_files)
            file = open(config.pidor_audio_files + random_audio_file, 'rb')

            bot.send_voice(message.chat.id, file)
            time.sleep(16)
            bot.send_message(message.chat.id, config.pidor_recognized + pidor_username)

        else:
            text_files = os.listdir(config.pidor_text_files)
            random_text_file = choice(text_files)
            file = open(config.pidor_text_files + random_text_file, 'r', encoding='utf-8')

            for line in file.readlines():
                bot.send_message(message.chat.id, line)
                time.sleep(2)

            bot.send_message(message.chat.id, '@' + pidor_username)

        file.close()
        config.pidor_registred.clear()
