from bs4 import BeautifulSoup
import requests


def imdb():
    try:
        response = requests.get(
            'https://www.imdb.com/search/title/?country_of_origin=ID')
        response.raise_for_status()
        S = BeautifulSoup(
            response.text, 'html.parser')
        database = S.find_all(
            'div', class_='lister-item mode-advanced')
        result = []

        for a in database:
            result.append({
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
            'author': 'VEXG',
            'result': result
        }
    except Exception as e:
        print(e)


print(imdb())
