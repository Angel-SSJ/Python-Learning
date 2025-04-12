import urllib.request

import json
from idlelib.rpc import response_queue

import requests

# 1. GET
# No puedes enviar un objetoo
print('\nGET:')
API_posts = 'https://jsonplaceholder.typicode.com/posts/'
response = requests.get(API_posts)
print(response.json())
response_json = response.json()
print(response_json[0])

# 2. POST

print('\nPOST')
try:
    response = requests.post('https://jsonplaceholder.typicode.com/posts/',
                             json={'userId': '2', "title": "esto es una request", "body": " estoy probando esta vaina"})
    #print(response.json())
    print(f"STATUS: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud: {e}')

# 3. PUT
print('\nPUT:')
#Actualizar un recurso
try:
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1',
                            json={'userId': '2', "title": "esto es una request", "body": " estoy probando esta vaina",
                                  'id': 1})
    #print(response.json())
    print(f"STATUS: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud:{e}')

#DIFERENCIA ENTRE PUT Y PATCH
#Put deberias pasarle ttodo le objeto  para volver a actualizarlo y con patch solo pasas las partes que deseas actualizar
#Put es mas completo y patch es mas localizado


# METODO HTTP QUERY
print('\nQUERY:')
# Es una mezcal entre Get y Post
# Tendria la parte de Get de recuperar el recurso y la parte de post de enviar el body


#-----------------------------------------------------------#