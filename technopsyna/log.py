import logging
from functools import wraps
from aiogram import types


def log(func):
    @wraps(func)
    async def log_wrapper(message: types.Message, *args, **kwargs):
        logging.debug(message.text)
        await func(message, *args, **kwargs)

    return log_wrapper
