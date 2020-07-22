from datetime import datetime
from functools import wraps
from random import random

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from technopsyna import config, larin, utils
from technopsyna.bl import get_bl, get_bl_string_message
from technopsyna.checker import UserHeap
from technopsyna.wolfram import (
    wolfram_parser,
    WolframEmptyQueryException,
    WolframQueryNotFoundException
)

bot = Bot(config.token)
dispatcher = Dispatcher(bot)
users = UserHeap()


def log(func):
    @wraps(func)
    async def log_wrapper(message: types.Message, *args, **kwargs):
        log_text = f'{datetime.now()}\n text: {message.text}\n'
        await bot.send_message(config.logs_channel, log_text)
        await func(message, *args, **kwargs)

    return log_wrapper


@dispatcher.message_handler(commands=config.text_commands)
@log
async def text_command(message: types.Message):
    command = message.get_command(pure=True)

    with open(utils.get_command_text_file(command), 'r') as file:
        await message.reply(
            file.read().strip(),
            parse_mode=types.ParseMode.MARKDOWN, disable_web_page_preview=True
        )


@dispatcher.message_handler(commands=list(config.ege_countdown_commands))
@log
async def ege_countdown_command(message: types.Message):
    command = message.get_command(pure=True)
    date_string, subject_name = config.ege_countdown_commands[command]
    days_left = utils.get_days_until(datetime.fromisoformat(date_string))
    await message.reply(f'До егэ по *{subject_name}* осталось {days_left} дней.',
                        parse_mode=types.ParseMode.MARKDOWN)


@dispatcher.message_handler(commands=['larin'])
@log
async def larin_command(message: types.Message):
    await message.reply(f'🧠 последний [вариант]({larin.get_latest_var_url()}) Ларина', parse_mode=types.ParseMode.MARKDOWN)


@dispatcher.message_handler(content_types=['new_chat_members'])
async def new_member_check(message: types.Message):
    chat_name = message.chat.title

    if chat_name != config.technoconfa_chatname:
        return

    user = message.new_chat_members[0]
    username = '@' + user.username if user.username else user.first_name
    users.add(user.id)
    user_alive_button = types.InlineKeyboardButton(
        'Да',
        callback_data=f'alive {username} {user.id}'
    )
    user_alive_keyboard = types.InlineKeyboardMarkup().add(user_alive_button)

    await bot.restrict_chat_member(
        message.chat.id, user.id,
        can_send_messages=False, can_add_web_page_previews=False,
        can_send_media_messages=False, can_send_other_messages=False
    )

    await bot.send_message(
        message.chat.id, f'Привет, {username}! Вы с нами?',
        reply_markup=user_alive_keyboard
    )


@dispatcher.callback_query_handler(lambda callback: callback.data.startswith('alive'))
async def handle_alive_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    user_id = int(callback_query.data.split()[2])
    username = callback_query.data.split()[1]
    chat_id = callback_query.message.chat.id

    if user_id != callback_query.from_user.id:
        return

    await bot.restrict_chat_member(
        chat_id, user_id,
        can_send_messages=True, can_add_web_page_previews=True,
        can_send_media_messages=True, can_send_other_messages=True
    )
    await bot.send_message(
        chat_id,
        f'{username} с нами! Представтесь, пожалуйста, '
        'или вы будете автоматически удалены через несколько часов.',
        reply_markup=types.ForceReply(selective=True)
    )
    await bot.send_sticker(chat_id, config.new_member_sticker)
    await callback_query.message.delete()


@dispatcher.message_handler(commands=['matan'])
@log
async def matan_command(message: types.Message):
    if message.from_user.id == config.my_id:
        with open(config.matan_image, 'rb') as image:
            await bot.send_photo(message.chat.id, image)


@dispatcher.message_handler(commands=['dembel'])
@log
async def dembel_command(message: types.Message):
    await message.reply(config.dembel_message,
                        parse_mode=types.ParseMode.MARKDOWN)


@dispatcher.message_handler(commands=['wf'])
@log
async def wolfram_command(message: types.Message):
    try:
        result, ratio = wolfram_parser(message.text)
        await bot.send_chat_action(
            message.chat.id,
            types.ChatActions.UPLOAD_PHOTO
        )

        if ratio > config.wolfram_max_ratio:
            await message.reply_document(result)
        else:
            await message.reply_photo(result)

    except WolframEmptyQueryException:
        await message.reply(
            'Использование: `/wf <запрос>`',
            parse_mode=types.ParseMode.MARKDOWN
        )

    except WolframQueryNotFoundException:
        await message.reply(
            'Запрос не найдён.\n'
            'Если вы ввели его на русском, '
            'то попробуйте ввести его на английском.'
        )


@dispatcher.message_handler(regexp=r'.*(витёк|витек).*')
@dispatcher.message_handler(commands=['vitek'])
@log
async def vitek(message: types.Message):
    with open(config.vitek_voice, 'rb') as voice_file:
        await bot.send_voice(message.chat.id, voice_file)


@dispatcher.message_handler(commands=['bl'])
@log
async def bl_command(message: types.Message):
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
    elif result.startswith('<sticker>'):
        sticker_id = result[9:].strip()
        await message.reply_sticker(sticker_id)
    else:
        await message.reply(result.replace('<br>', '\n'))


@dispatcher.message_handler(regexp=r'.*ыыы.*')
async def bl_string_message(message: types.Message):
    answer = get_bl_string_message()
    if answer:
        await message.reply(answer)


@dispatcher.message_handler(regexp=config.chto_pacani_pattern)
@log
async def chto_pacani(message: types.Message):
    await message.reply_sticker(config.cho_pacani_sticker)


@dispatcher.message_handler(regexp=r'.*')
async def new_member_checker(message: types.Message):
    if message.chat.title != config.technoconfa_chatname:
        return

    if larin.is_check_time():
        next_var = larin.get_next_var_url()
        if next_var:
            await bot.send_message(message.chat.id, f'🌱 вышел новый [вариант]({next_var}) Ларина', parse_mode=types.ParseMode.MARKDOWN)

    if message.from_user.id in users.table:
        users.delete(message.from_user.id)
        await message.reply('Вы приняты.')

    if not users.is_check_time():
        return
    for user_id in users.check():
        await (await bot.get_chat(message.chat.id)).kick(user_id)


if __name__ == '__main__':
    executor.start_polling(dispatcher)
