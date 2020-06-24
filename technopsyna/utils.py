from technopsyna import config
from datetime import datetime


def get_relative_command(full_command):
    return full_command.replace(config.bot_username, '')[1:]


def get_days_until(date):
    delta = date - datetime.now()
    return delta.days


def get_command_text_file(command):
    return f'technopsyna/static/commands/{command}'
