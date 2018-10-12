import io
import requests
from PIL import Image

import config


def crop_image(image):
    original_img = Image.open(io.BytesIO(image))
    cropped_img = original_img.crop((0, 95, 540, original_img.size[1] - 50))
    io_img = io.BytesIO()
    io_img.name = 'wolfram.png'
    cropped_img.save(io_img, format='png')
    io_img.seek(0)

    return io_img, cropped_img.size[1] / cropped_img.size[0]


def wolfram_parser(query):
    try:
        query = query.split(maxsplit=1)[1]
    except IndexError:
        return 0, None, None

    response = requests.get(config.wolfram_url, params={'i': query})
    if response.status_code == 200:
        return 1, crop_image(response.content)

    else:
        return -1, None, None
