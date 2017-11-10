import io
import requests
from PIL import Image
from telebot import types

import config
from bot import bot


def wolfram_parser(query):
    if not len(query.split()) == 0:
        response = requests.get("https://api.wolframalpha.com/v1/simple?appid=" + config.wolfram_appid,
                                params={'i': query})

        if response.status_code == 200:
            img_original = Image.open(io.BytesIO(response.content))
            img_cropped = img_original.crop((0, 95, 540, img_original.size[1] - 50))
            io_img = io.BytesIO()
            io_img.name = "wolfram {}.png".format(query.replace("/", "_"))
            img_cropped.save(io_img, format="png")
            io_img.seek(0)

            return [0, io_img, img_cropped.size[1] / img_cropped.size[0]]

        else:
            return [-1, "bad_status"]

    return [-1, "empty"]


def wolfram_command(message):
    response = wolfram_parser(' '.join(message.text.split()[1:]))

    if response[0] == 0:
        bot.send_chat_action(message.chat.id, 'upload_photo')
        wolfram_max_ratio = 2.5
        if response[2] > wolfram_max_ratio:
            bot.send_document(message.chat.id, response[1], reply_to_message_id=message.message_id)
        else:
            bot.send_photo(message.chat.id, response[1], reply_to_message_id=message.message_id)

    else:
        if response[1] == "bad_status":
            bot.reply_to(message, config.wolfram_bad_status_message)

        else:
            bot.reply_to(message, config.wolfram_empty_query_message, parse_mode="Markdown")


def wolfram_inline(query):
    response = wolfram_parser(' '.join(query.query.split()[1:]))

    if response[0] == 0:
        wolfram_max_ratio = 2.5
        if response[2] > wolfram_max_ratio:
            d = bot.send_document(int(config.my_id), response[1])
            r = types.InlineQueryResultCachedDocument(id='1', title=response[1].name,
                                                      document_file_id=d.document.file_id)
            bot.answer_inline_query(query.id, [r])

        else:
            p = bot.send_photo(int(config.my_id), response[1])
            r = types.InlineQueryResultCachedPhoto(id='1', photo_file_id=p.photo[-1].file_id)
            bot.answer_inline_query(query.id, [r])
