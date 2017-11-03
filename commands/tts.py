import os
from gtts import gTTS

from bot import bot


def text_to_speech(message):
    voice = gTTS(text=' '.join(message.text.split()[1:]), lang='ru')
    voice.save("voice_file.ogg")

    voice_file = open("voice_file.ogg", "rb")
    bot.send_voice(message.chat.id, voice_file, reply_to_message_id=message.message_id)

    os.remove("voice_file.ogg")