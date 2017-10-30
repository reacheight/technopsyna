import telebot

import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['bl'])
def bl_command(message):
    bot.send_message(message.chat.id, config.bl_string())


@bot.message_handler(content_types=['text'])
def bl_message(message):
    if 'ыыы' in message.text:
        bot.reply_to(message, config.bl_string())


bot.polling(none_stop=True)
