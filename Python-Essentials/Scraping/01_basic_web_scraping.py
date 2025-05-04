# NO ES ILEGAL

import requests
import re

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'

response =requests.get(url)
html=response.text
if response.status_code == 200:
    print('La solicitud fue exitosa')
    #print(html)
else:
    print(f'Error en la solicitud: {response.status_code}')

# regular expression para encotrar el precio

print('-----------------')
price_pattern = r'<span class="rc-prices-fullprice">(.+?)</span>'

try:
    match=re.search(price_pattern,html)
    print(f'el precio es: {match.group(1)}')
except AttributeError:
    print('No se encontró el precio')