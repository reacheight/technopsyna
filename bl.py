import os
from random import choice, randint, random

import config


def get_bl_string_message():
    probability = random()
    if probability <= 0.1:
        return 'ы' * randint(5, 20)
    if probability >= 0.9:
        return 'Прекратите!'


def get_bl():
    if random() <= 0.05:
        images = os.listdir(config.bl_images_locations)
        return 'img', choice(images)

    else:
        with open(config.bl_text_file, 'r', encoding='utf-8') as bl_file:
            return 'txt', choice(list(bl_file)).rstrip()
