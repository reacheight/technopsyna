import io
import requests
from PIL import Image

from technopsyna import config


class WolframEmptyQueryException(Exception):
    pass


class WolframQueryNotFoundException(Exception):
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
        raise WolframEmptyQueryException
    response = requests.get(config.wolfram_url, params={'i': query[1]})
    if response.status_code != 200:
        raise WolframQueryNotFoundException
    return crop_image(response.content)
