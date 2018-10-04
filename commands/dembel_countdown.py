from datetime import date

import config
from techconfbot import bot


def count_of_days_before_dmb():
    dmb_date = date(config.deer_dembel_date['year'],
                    config.deer_dembel_date['month'],
                    config.deer_dembel_date['day'])

    delta = dmb_date - date.today()

    return delta.days


def dembel_command(message):
    bot.send_message(message.chat.id,
                     "До дембеля Оленя осталось *" + str(count_of_days_before_dmb()) + "* дней!",
                     parse_mode="Markdown")