# experiment : scraping tebak gambar
# the modules // module nya
from bs4 import BeautifulSoup
import requests
import random


def tebak_gambar():  # functions
    try:  # trying the code below, if got an err. then move to execption // mencoba code dibawah ini, jika terdapat err. pindah ke execption
        # random number from 0 - 2600 // angka acak dari 0-2600
        angka = str(random.randint(0, 2600))
        get_response = requests.get(
            f'https://jawabantebakgambar.net/id-{angka}.html')
        # geting the status response // mendapatkan status code respon dari webnya
        get_response.raise_for_status()
        get_soup = BeautifulSoup(
            get_response.text, 'html.parser')  # parsing the HTML // memparsing HTML

        return {
            'creator': 'VEXG/Helmi',  # please dont change this // jan di ganti yaak :v
            'result': {
                # getting the image link // mendapatkan link foto
                'image': str(get_soup.find('ul', id='images').li.a.img.get('src')),
                # getting the answer // mendapatkan jawaban tebak gambar
                'answer': str(get_soup.find('div', class_='content').p.b.text)
            }
        }
    except Exception as e:  # catch error // menangkap errornya
        print(e)  # print the err // mengprint atau mengoutput error


# calling or print the functions // mengcall atau mengprint functions nya
print(tebak_gambar())

# what i learned from this experiment:
# using requests and beautifulSoup
# make a func
# making a rand number
# getting response code from web
# try/except
