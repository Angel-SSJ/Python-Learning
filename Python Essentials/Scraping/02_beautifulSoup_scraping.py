import requests
from bs4 import BeautifulSoup
url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}# Osea que mandamos que nos conectamos con esto(este dispositivo)
response= requests.get(url, headers=headers)

if response.status_code == 200:
    print('La solicitud fue exitosa')
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

    title_tag=soup.title.text
    print(f'Titulo: {title_tag}')
    title_tag=soup.title.string
    print(f'Titulo: {title_tag}')

    metas=soup.title.parent.find_all('meta')
    print(f'Metas: {metas}')
else:
    print(f'Error en la solicitud: {response.status_code} CTM')



# find price using bs4
soup = BeautifulSoup(response.text, 'html.parser')
price=soup.find('span', class_='rc-prices-fullprice')
print(f'price: {price.string}')
# find every price using bs4
prices = soup.find_all('span',class_='rc-prices-fullprice') # el span es opcional
for price in prices:

    print(f'price: {price.string}')

# find each product and get name and the price
soup = BeautifulSoup(response.text, 'html.parser')
products = soup.find_all(class_="rc-productbundle-details")
for product in products:
    name = product.find(class_='list-title rc-productbundle-title typography-label')
    price = product.find(class_="rc-prices-fullprice").text
    print(f'Producto:{name} con precio: {price}')




# User-Agent de google
#https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers?hl=es