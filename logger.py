import config
from bot import bot

from datetime import datetime


def log(message):
    log_text = f'{str(datetime.now())}\n' \
               f'text: { message.text}\n'

    bot.send_message(config.logs_channel, log_text)
