import config
from techconfbot import bot

from datetime import datetime


def log(message):
    log_text = str(datetime.now()) + '\n'
    log_text += 'text: ' + message.text + '\n'

    bot.send_message(config.logs_channel, log_text)
