import config
from bot import bot

from datetime import datetime


def log(message):
    log_text = str(datetime.now()) + '\n'
    log_text += 'username: @' + str(message.from_user.username) + '\n'
    log_text += 'user id: ' + str(message.from_user.id) + '\n'
    log_text += 'text: ' + message.text + '\n'

    bot.send_message(config.my_id, log_text)
