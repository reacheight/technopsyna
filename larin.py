import config
import redis

db = redis.from_url(config.redis_url)


def get_latest_var_url():
    var_number = db.get(config.larin_var_key)
    return config.larin_variant_pdf_template.format(var_number)
