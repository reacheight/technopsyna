from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from random import random
from datetime import datetime

from wolfram import wolfram_parser
from wolfram import WrongLenWolframQueryException, ResponceCodeNo200
from bl import get_bl, get_bl_string_message
from dembel_countdown import get_dembel_string
import config

bot = Bot(config.token)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=list(config.text_commands.keys()))
async def text_command(message: types.Message):
    await log(message)
    command = message.text.split('@', 1)[0][1:]

    with open(config.text_commands[command], 'r') as file:
        await message.reply(file.read().strip(),
                            parse_mode=types.ParseMode.MARKDOWN,
                            disable_web_page_preview=True)


@dispatcher.message_handler(content_types=['new_chat_members'])
async def new_member_greeting(message: types.Message):
    chat_name = message.chat.title

    if chat_name != config.technoconfa_chatname:
        return

    user = message.new_chat_members[0]
    username = '@' + user.username if user.username else user.first_name

    await bot.send_message(message.chat.id,
                           f'Привет, {username}! Представься, пожалуйста.')
    await bot.send_sticker(message.chat.id, config.new_member_sticker)


@dispatcher.message_handler(commands=['matan'])
async def matan_command(message: types.Message):
    await log(message)
    if message.from_user.id == config.my_id:
        with open(config.matan_image, 'rb') as image:
            await bot.send_photo(message.chat.id, image)


@dispatcher.message_handler(commands=['dembel'])
async def dembel_command(message: types.Message):
    await log(message)
    await message.reply(get_dembel_string(),
                        parse_mode=types.ParseMode.MARKDOWN)


@dispatcher.message_handler(commands=['wf'])
async def wolfram_command(message: types.Message):
    await log(message)
    try:
        result, ratio = wolfram_parser(message.text)
        await bot.send_chat_action(message.chat.id,
                                   types.ChatActions.UPLOAD_PHOTO)

        if ratio > config.wolfram_max_ratio:
            await message.reply_document(result)
        else:
            await message.reply_photo(result)

    except WrongLenWolframQueryException:
        await message.reply('Использование: `/wf <запрос>`',
                            parse_mode=types.ParseMode.MARKDOWN)

    except ResponceCodeNo200:
        await message.reply('Запрос не найдён.\n'
                            'Если ты ввёл его на русском, '
                            'то попробуй ввести его на английском.')


@dispatcher.message_handler(commands=['bl'])
async def bl_command(message: types.Message):
    await log(message)
    if message.chat.title == config.technoconfa_chatname and random() > 0.7:
        await bot.send_message(message.chat.id, 'Не флудите.')
        return

    bl_type, result = get_bl()

    if bl_type == 'img':
        with open(config.bl_images_locations + result, 'rb') as image:
            if result.endswith('.gif'):
                await message.reply_document(image)
            else:
                await message.reply_photo(image)
    else:
        if result.startswith('<sticker>'):
            sticker_id = result[9:].strip()
            await message.reply_sticker(sticker_id)

        else:
            await message.reply(result.replace('<br>', '\n'))


@dispatcher.message_handler(regexp=r'.*ыыы.*')
async def bl_string_message(message: types.Message):
    string = get_bl_string_message()
    if string is not None:
        await message.reply(string)


@dispatcher.message_handler(regexp=config.chto_pacani_pattern)
async def chto_pacani(message: types.Message):
    await message.reply_sticker(config.cho_pacani_sticker)


async def log(message):
    log_text = f'{datetime.now()}\n text: {message.text}\n'

    await bot.send_message(config.logs_channel, log_text)


executor.start_polling(dispatcher)
