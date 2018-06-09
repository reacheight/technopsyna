import config
from bot import bot


def passing_scores(message):
    with open(config.passing_scores_file, 'r') as file:
        bot.send_message(message.chat.id, file.read().strip(),
                         parse_mode='Markdown', disable_web_page_preview=True)