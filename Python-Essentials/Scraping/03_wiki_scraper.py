import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_url(url:str):
    response = requests.get(url)
    if response.status_code == 200:
        print('La solicitud fue exitosa')
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraer todos los titulos <h1>
        titles=[title.string for title in soup.find_all('h1')] # este tipo de lista tiene un nombre xd, no me acuerdo
        print(f'Titulos: {titles}')

        #Extraer todos los enlaces
        links=[link.get('href') for link in soup.find_all('a')]
        print(f'Links: {links}')# EsTOS SON enlaces relativos

        links=[urljoin(url,link.get('href')) for link in soup.find_all('a')]
        print(f'Links absolutos: {links}')# Estos son enlaces absolutos

        #for link in links:
        #    scrape_url(link)
        #    sleep(10)



scrape_url(url='https://en.wikipedia.org/wiki/Web_scraping')



#Extraer tdo el contenido de la pagina de texto
url='https://en.wikipedia.org/wiki/Web_scraping'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
all_text = soup.find('main').get_text()
print(f'Texto: {all_text}')


# Extraer de la id mw-content-text
content_text = soup.find('p').get_text()
print(f'Texto: {content_text}')


# Extraer el open graph si existe

url='https://midu.dev'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
og_image=soup.find('meta', {'property':'og:image'})
if og_image:
    print(f'Image: {og_image['content']}')
else:
    print('No se encontro la imagen CTM')
    
og_image=soup.find('meta', property='og:image')
if og_image:
    print(f'Image: {og_image['content']}')
else:
    print('No se encontro la imagen CTM')
