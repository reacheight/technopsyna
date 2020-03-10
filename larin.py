import config
import redis
import requests

db = redis.from_url(config.redis_url)


def get_latest_var_url():
    current_var_number = int(db.get(config.larin_var_key).decode('utf-8'))
    next_var = get_next_var_url(current_var_number)
    return next_var if next_var else config.larin_variant_pdf_template.format(current_var_number)


def get_next_var_url(current_var_number):
    var_number = current_var_number + 1
    var_url = config.larin_variant_pdf_template.format(var_number)
    request = requests.get(var_url)
    if request.status_code == 200:
        db.set(config.larin_var_key, var_number)
        return var_url
