import os
from gtts import gTTS
from telebot import types

import config
from bot import bot


def create_voice_file(text):
    splited_text = text.split(maxsplit=1)
    if len(splited_text) > 1:
        voice = gTTS(splited_text[1], lang='ru')
        voice.save("voice_file.ogg")


def text_to_speech(message):
    create_voice_file(message.text)

    if "voice_file.ogg" in os.listdir(os.curdir):
        voice_file = open("voice_file.ogg", "rb")
        bot.send_voice(message.chat.id, voice_file, reply_to_message_id=message.message_id)
        os.remove("voice_file.ogg")

    else:
        bot.reply_to(message, config.tts_empty_query_message, parse_mode="Markdown")


def text_to_speech_inline(query):
    create_voice_file(query.query)

    if "voice_file.ogg" in os.listdir(os.curdir):
        voice_file = open("voice_file.ogg", "rb")
        v = bot.send_voice(int(config.my_id), voice_file)

        r = types.InlineQueryResultCachedVoice(id='1', voice_file_id=v.voice.file_id, title="voice")
        bot.answer_inline_query(query.id, [r])
        os.remove("voice_file.ogg")
