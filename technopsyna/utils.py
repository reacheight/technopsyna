from technopsyna import config
from datetime import datetime


def get_days_until(date):
    delta = date - datetime.now()
    return delta.days


def get_command_text_file(command):
    return f'technopsyna/static/commands/{command}'
