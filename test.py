from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import config

bot = Bot(config.test_token)
dispatcher = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dispatcher)
