# Como hacer peticiones a APIs con Python
# con y sin dependencias

# 1. DIFICIL Y SIN DEPENDENCIAS
import urllib.request
# biblioteca simple que nos permite abrir una url con diferentes protocolos y somos nosotros los que decide como tiene que leer la respuesta, decodificar xd
import json
# Para transformar la respuesta
try:
    API_posts ='https://jsonplaceholder.typicode.com/posts/'
    response = urllib.request.urlopen(API_posts) # Va a esa url y la abre a saco
    data = response.read() # Lee los datos :D
    json_data =json.loads(data.decode('utf-8')) # el carga desde json los datos con encoding utf-8
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f'Error en la solicitud: {e.reason}')

#CON DEPENDENCIAS (requests)
import requests

print('\nGET:')
response = requests.get(API_posts)
print(response.json())
json= response.json()
print(json[0])


# METODO HTTP PULL

# 3. Un post
print('\nPOST')
try:
    input={'userId':'2', "title":"esto es una request", "body":" estoy probando esta vaina"}
    response= requests.post(API_posts, json=input)
    print(response.json())
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud: {e}')

# METODO HTTP POST



