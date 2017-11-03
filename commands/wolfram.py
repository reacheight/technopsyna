import io
import requests
from PIL import Image

import config
from bot import bot


def wolfram_solver(message):

    if not len(message.text.split()) == 1:
        bot.send_chat_action(message.chat.id, 'upload_photo')
        your_query = ' '.join(message.text.split()[1:])
        response = requests.get("https://api.wolframalpha.com/v2/simple?appid=" + config.wolfram_appid + "&i=" + your_query)

        if response.status_code == 200:
            img_original = Image.open(io.BytesIO(response.content))
            img_cropped = img_original.crop((0, 95, 540, img_original.size[1] - 50))
            io_img = io.BytesIO()
            io_img.name = "wolfram {}.png".format(your_query.replace("/", "_"))
            img_cropped.save(io_img, format="png")
            io_img.seek(0)
            wolfram_max_ratio = 2.5
            if img_cropped.size[1] / img_cropped.size[0] > wolfram_max_ratio:
                bot.send_document(message.chat.id, io_img, reply_to_message_id=message.message_id)
            else:
                bot.send_photo(message.chat.id, io_img, reply_to_message_id=message.message_id)

        else:
            bot.reply_to(message, config.wolfram_bad_status_message)

    else:
        bot.reply_to(message, config.wolfram_empty_query_message, parse_mode="Markdown")
