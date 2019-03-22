import io
import requests
from PIL import Image

import config


class WrongLenWolframQueryException(Exception):
    pass


class ResponceCodeNo200(Exception):
    pass


def crop_image(image):
    original_img = Image.open(io.BytesIO(image))
    cropped_img = original_img.crop((0, 95, 540, original_img.size[1] - 50))
    io_img = io.BytesIO()
    io_img.name = 'wolfram.png'
    cropped_img.save(io_img, format='png')
    io_img.seek(0)

    return io_img, cropped_img.size[1] / cropped_img.size[0]


def wolfram_parser(query):
    query = query.split(maxsplit=1)
    if len(query) != 2:
        raise WrongLenWolframQueryException
    response = requests.get(config.wolfram_url, params={'i': query})
    if response.status_code != 200:
        raise ResponceCodeNo200
    return crop_image(response.content)
