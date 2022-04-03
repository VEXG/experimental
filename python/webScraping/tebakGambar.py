
from bs4 import BeautifulSoup
import requests
import random


def tebak_gambar():
    try:
        randNum = str(random.randint(0, 2600))
        response = requests.get(
            f'https://jawabantebakgambar.net/id-{randNum}.html')
        response.raise_for_status()
        S = BeautifulSoup(
            response.text, 'html.parser')

        return {
            'creator': 'VEXG',
            'result': {

                'image': str(S.find('ul', id='images').li.a.img.get('src')),

                'answer': str(S.find('div', class_='content').p.b.text)
            }
        }
    except Exception as e:
        print(e)


print(tebak_gambar())
