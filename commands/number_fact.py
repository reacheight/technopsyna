import requests
import re

import config
from bot import bot


def get_number_fact(number):
    return requests.get(config.number_api_url + number)


def type_number_fact(message):
    obj = re.search(config.integer_pattern, message.text)
    if not obj:
        bot.reply_to(message, config.number_fact_empty, parse_mode="Markdown")
        return

    bot.reply_to(message, get_number_fact(obj.group()))
