# experiment : scraping imdb
# the modules // module nya
from bs4 import BeautifulSoup
import requests


def imdb():  # functions
    try:  # trying the code below, if got an err. then move to execption // mencoba code dibawah ini, jika terdapat err. pindah ke execption
        get_response = requests.get(
            'https://www.imdb.com/search/title/?country_of_origin=ID')
        # geting the status response // mendapatkan status code respon dari webnya
        get_response.raise_for_status()
        get_soup = BeautifulSoup(
            get_response.text, 'html.parser')
        get_find = get_soup.find_all(
            'div', class_='lister-item mode-advanced')  # parsing the HTML // memparsing HTML
        get_arry = []  # this is an array, will be storing for the list // ini adalah array, akan di gunakan untuk menyimpan list

        for a in get_find:  # this is loop, get_find use .find_all to collect the list target from the web and putting into the array. so get_find can be looped // ini adalah loop, get_find menggunakan .find_all untuk mengambil list target pada web dan menaruhnya di array. jadi get_find bisa di loop
            get_arry.append({  # pushing / appending the info to array // pushing / appending info ke array
                # kinda complicated to explain it soo.. skip
                'title': a.find('h3', class_='lister-item-header').a.text.strip(),
                'released': a.find('h3', class_='lister-item-header').select_one('span:nth-of-type(2)').text.strip('()').replace(') (', ' ').replace('–', ' ').strip(),
                'duration': a.find('span', class_='runtime').text.strip() if a.find('span', class_='runtime') is not None else 'Unknown',
                'genre': a.find('span', class_='genre').text.strip() if a.find('span', class_='genre') is not None else 'Unknown',
                'rating': a.find('div', class_='inline-block ratings-imdb-rating').strong.text.strip() if a.find('div', class_='inline-block ratings-imdb-rating') is not None else 'Unknown',
                'votes': a.find('p', class_='sort-num_votes-visible').select_one('span:nth-of-type(2)').text if a.find('p', class_='sort-num_votes-visible') is not None else 'Unknown',
                'director': a.find('div', class_='lister-item-content').select_one('p:nth-of-type(3)').text.split('Director:\n')[1].split('\n|')[0].strip() if 'Director:' in a.find('div', class_='lister-item-content').select_one('p:nth-of-type(3)').text else 'Unknown',
                'stars': a.find('div', class_='lister-item-content').select_one('p:nth-of-type(3)').text.split('Stars:')[1].replace('\n', '').strip() if 'Stars:' in a.find('div', class_='lister-item-content').select_one('p:nth-of-type(3)').text else 'Unknown',
                'link': 'https://www.imdb.com' + a.find('h3', class_='lister-item-header').a.get('href'),
                'thumbnail': a.select_one('div > div > div:nth-of-type(2) > a > img').get('src'),
                'description': a.find('div', class_='lister-item-content').select_one('p:nth-of-type(2)').text.strip().replace('Add a Plot', 'Unknown')
            })
        return {
            'creator': 'VEXG/Helmi',
            'result': get_arry
        }
    except Exception as e:  # catch error // menangkap errornya
        print(e)  # print the err // mengprint atau mengoutput error


# calling or print the functions // mengcall atau mengprint functions nya
print(imdb())

# what i learned from this experiment:
# find_all functions
# looping
# array append functions
# strip functions
# if things (kinda better than javascript if)
# select_one functions
