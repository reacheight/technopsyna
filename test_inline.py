# _*_ coding: utf-8 _*_
from bot import bot
from telebot import types
import requests
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientRateLimitError
from PIL import Image
import io
import os
from gtts import gTTS

client_id = 'e4e2861f23b7b5d'
client_secret = '6bbf057be1eb6dce60f2d03111f28b8749ddca46'

client = ImgurClient(client_id, client_secret)

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
# @bot.message_handler(commands=['wf'])
# def test(message):
    if query.query.split()[0] == 'wf':
        your_query = ' '.join(query.query.split()[1:])
        response = requests.get("https://api.wolframalpha.com/v2/simple?appid=" + '7PKA2K-Y8ULYG5TAY' + "&i=" + your_query)

        if response.status_code == 200:
            img_original = Image.open(io.BytesIO(response.content))
            img_cropped = img_original.crop((0, 95, 540, img_original.size[1] - 50))
            io_img = io.BytesIO()
            io_img.name = "wolfram {}.png".format(your_query.replace("/", "_"))
            img_cropped.save(io_img, format="png")
            io_img.seek(0)
            # f = open("test.jpeg", "wb")
            # f.write(io_img.read())
            # f.close()
            # f = open("test.jpeg", "rb")
            # r = bot.send_photo(279261596, f)
            # f.close()
            wolfram_max_ratio = 2.5
            if img_cropped.size[1] / img_cropped.size[0] > wolfram_max_ratio:
                d = bot.send_document(279261596, io_img)
                r = types.InlineQueryResultCachedDocument(id='1', title=io_img.name, document_file_id=d.document.file_id)
                bot.answer_inline_query(query.id, [r])
            else:
                p = bot.send_photo(279261596, io_img)
                r = types.InlineQueryResultCachedPhoto(id='1', photo_file_id=p.photo[-1].file_id)
                bot.answer_inline_query(query.id, [r])

    else:
        if len(query.query.split()) > 1:
            voice = gTTS(text=' '.join(query.query.split()[1:]), lang='ru')
            voice.save("voice_file.ogg")

        if "voice_file.ogg" in os.listdir(os.curdir):
            voice_file = open("voice_file.ogg", "rb")
            v = bot.send_voice(279261596, voice_file)

            r = types.InlineQueryResultCachedVoice(id='1', voice_file_id=v.voice.file_id, title="voice")
            bot.answer_inline_query(query.id, [r])
            os.remove("voice_file.ogg")


        # try:
        #     image = client.upload_from_path("test.jpeg")
        #     # wf = client.upload_from_path("wf.jpg")
        #     r = types.InlineQueryResultPhoto(id='1', photo_url=image['link'], thumb_url="https://i.imgur.com/mZmHcfq.jpg")
        #     bot.answer_inline_query(query.id, [r])
        # except ImgurClientRateLimitError as e:
        #     print(client.credits)

@bot.message_handler(commands=['test'])
def test(message):
    # image = client.upload_from_path("wf.jpg")
    # r = requests.post("http://telegra.ph/upload/", files={'file': open('wf.jpg')})
    bot.send_message(message.chat.id, message.from_user.id)


bot.polling(none_stop=True)
