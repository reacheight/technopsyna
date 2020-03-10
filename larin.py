import config
import redis
import requests
from datetime import datetime

db = redis.from_url(config.redis_url)
last_check_time = datetime.now()


def get_latest_var_url():
    next_var = get_next_var_url()
    return next_var if next_var else get_current_var_url()


def get_current_var_url():
    current_var_number = int(db.get(config.larin_var_key).decode('utf-8'))
    return config.larin_variant_pdf_template.format(current_var_number)


def get_next_var_url():
    global last_check_time
    last_check_time = datetime.now()

    current_var_number = int(db.get(config.larin_var_key).decode('utf-8'))
    next_var_number = current_var_number + 1
    next_var_url = config.larin_variant_pdf_template.format(next_var_number)

    request = requests.get(next_var_url)
    if request.status_code == 200:
        db.set(config.larin_var_key, next_var_number)
        return next_var_url


def is_check_time():
    return datetime.now() - last_check_time >= config.larin_check_time
