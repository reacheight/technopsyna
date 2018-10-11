from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import config

bot = Bot(config.token)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=list(config.text_commands.keys()))
async def text_command(message: types.Message):
    command = message.text.split('@', 1)[0][1:]

    with open(config.text_commands[command], 'r') as file:
        await message.reply(file.read().strip(), parse_mode=types.ParseMode.MARKDOWN,
                            disable_web_page_preview=True)


@dispatcher.message_handler(content_types=['new_chat_members'])
async def new_member_greeting(message: types.Message):
    chat_name = message.chat.title

    if chat_name != config.technoconfa_chatname:
        return

    user = message.new_chat_members[0]
    username = '@' + user.username if user.username else user.first_name

    await bot.send_message(message.chat.id, f'Привет, {username}! Представься, пожалуйста.')
    await bot.send_sticker(message.chat.id, config.new_member_sticker)


@dispatcher.message_handler(commands=['matan'])
async def matan_command(message: types.Message):
    if message.from_user.id == config.my_id:
        with open(config.matan_image, 'rb') as image:
            await bot.send_photo(message.chat.id, image)


@dispatcher.message_handler(regexp=config.chto_pacani_pattern)
async def chto_pacani(message: types.Message):
    await message.reply_sticker(config.cho_pacani_sticker)

executor.start_polling(dispatcher)
