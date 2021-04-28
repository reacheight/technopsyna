import re

import requests
from bs4 import BeautifulSoup

base_url = {
    'math': 'https://ege.sdamgia.ru',
    'rus': 'https://rus-ege.sdamgia.ru',
    'inf': 'https://inf-ege.sdamgia.ru',
    'phys': 'https://phys-ege.sdamgia.ru'
}

max_tasks = {
    'math': 19,
    'rus': 27,
    'inf': 27,
    'phys': 32
}


def generate_variant(subject, tasks):
    default_task_count = 0 if len(tasks) > 0 else 1
    form_data = {f'prob{i}': default_task_count for i in range(1, max_tasks[subject] + 1)}
    for task in tasks:
        form_data[f'prob{task}'] += 1

    generate_response = requests.post(f'{base_url[subject]}/test?a=generate', data=form_data)
    generate_response.raise_for_status()

    test_page = BeautifulSoup(generate_response.text, 'html.parser')
    variant_number = test_page.find('b', string=re.compile('.*Вариант №.*')).text.split()[-1]
    return f'{base_url[subject]}/test?id={variant_number}&print=true&num=true&pdf=z'
