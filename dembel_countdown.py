from datetime import date

import config


def number_of_days_before_dmb():
    dmb_date = date(config.deer_dembel_date['year'],
                    config.deer_dembel_date['month'],
                    config.deer_dembel_date['day'])

    delta = dmb_date - date.today()
    return delta.days


def get_dembel_string():
    return f'До дембеля Оленя осталось *{number_of_days_before_dmb()}* дней!'
