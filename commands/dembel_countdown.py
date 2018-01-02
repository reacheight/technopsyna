from datetime import date

import config
from bot import bot


def get_count_of_days_befor_dmb():
    dmb_date = date(config.deer_dembel_date['year'], config.deer_dembel_date['month'], config.deer_dembel_date['day'])
    delta = dmb_date - date.today()

    return delta.days


def dmb_days(message):
    bot.reply_to(message, "До дембеля Оленя осталось *" + str(get_count_of_days_befor_dmb()) + "* дней!",
                 parse_mode="Markdown")