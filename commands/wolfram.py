import io
import requests
from PIL import Image
from telebot import types

import config
from bot import bot

wolfram_max_ratio = 2.5


def wolfram_parser(query):
    try:
        query = query.split(maxsplit=1)[1]
    except IndexError:
        return 0, None, None

    response = requests.get(config.wolfram_url, params={'i': query})

    if response.status_code == 200:
        original_img = Image.open(io.BytesIO(response.content))
        cropped_img = original_img.crop((0, 95, 540, original_img.size[1] - 50))
        io_img = io.BytesIO()
        io_img.name = 'wolfram {}.png'.format(query.replace('/', '_'))
        cropped_img.save(io_img, format='png')
        io_img.seek(0)

        return 1, io_img, cropped_img.size[1] / cropped_img.size[0]

    else:
        return -1, None, None


def wolfram_command(message):
    code, result, ratio = wolfram_parser(message.text)

    if code == 1:
        bot.send_chat_action(message.chat.id, 'upload_photo')

        if ratio > wolfram_max_ratio:
            bot.send_document(message.chat.id, result, reply_to_message_id=message.message_id)
        else:
            bot.send_photo(message.chat.id, result, reply_to_message_id=message.message_id)

    elif code == -1:
        bot.reply_to(message, 'Запрос не найдён.\n'
                              'Если ты ввёл его на русском, то попробуй ввести его на английском.')

    elif code == 0:
        bot.reply_to(message, 'Использование: `/wf <запрос>`', parse_mode='Markdown')


def wolfram_inline(query):
    code, result, ratio = wolfram_parser(query.query)

    if code != 1:
        return

    if ratio > wolfram_max_ratio:
        message = bot.send_document(config.my_id, result)
        response = types.InlineQueryResultCachedDocument(id='1', title=result.name,
                                                         document_file_id=message.document.file_id)
        bot.answer_inline_query(query.id, [response])

    else:
        message = bot.send_photo(config.my_id, result)
        response = types.InlineQueryResultCachedPhoto(id='1', photo_file_id=message.photo[-1].file_id)
        bot.answer_inline_query(query.id, [response])
