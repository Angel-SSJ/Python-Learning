# programa para revisar rapidamente el CEO de una pagina we, poner algunos colores en la terminal y saber como leer argumentos de la linea de comandos

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import argparse #parseador de argumentos

parser = argparse.ArgumentParser(description='Web scraping to check SEO for a given URL.')
parser.add_argument('url',type=str,help='the URL of the site you want to scrape and check')
args = parser.parse_args()
url = args.url

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('La solicitud fue exitosa')
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'\033[36mRevisando la pagina: {url}\033[0m')
    print('\n SEO basico:')

    title_page=soup.title.string#.encode('utf-8')
    if title_page:
        print(f'\033[36mTitulo:\033[0m {title_page}')
        if len(title_page)<70:
            print('Longitud del titulo es correcta')
        elif len(title_page)>70:
            print('Longitud del titulo es demasiado largo CTM ')
        else:
            print('Longitud del titulo es demasiado corto CTM')
    # Extrae todos los titulos h1

    titles= [title.text for title in soup.find_all('h1')]
    if not titles:
        print(f'\33[31mNo se encontraron titulos h1\33[0m')
    elif len(titles)>1:
        print(f'\033[31mHay mas de un titulo h1 en la web:\033[0m')
        for title in titles:
            print(title)
    else:
        print(f'\033[36mHay un titulo h1 en la website:\033[0m')