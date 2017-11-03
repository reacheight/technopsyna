import os
from gtts import gTTS

import config
from bot import bot


def text_to_speech(message):
    if len(message.text.split()) > 1:
        voice = gTTS(text=' '.join(message.text.split()[1:]), lang='ru')
        voice.save("voice_file.ogg")

        if "voice_file.ogg" in os.listdir(os.curdir):
            voice_file = open("voice_file.ogg", "rb")
            bot.send_voice(message.chat.id, voice_file, reply_to_message_id=message.message_id)
            os.remove("voice_file.ogg")

    else:
        bot.reply_to(message, config.tts_empty_query_message, parse_mode="Markdown")