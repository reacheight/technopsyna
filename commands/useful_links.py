import config
from bot import bot


def links(message):
    with open(config.links_list, "r") as f:
        bot.reply_to(message, f.read(), parse_mode="Markdown", disable_web_page_preview=True)
