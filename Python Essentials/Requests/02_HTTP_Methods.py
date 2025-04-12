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
## Usar la API de GPT-4o de OPENAI

OPENAI_KEY ='sk-xxxxxxxx'


def call_openai_gpt(api_key, prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        "model": "gpt-4o-mini",
        "message": [
            {
                'role': 'user',
                'content': prompt
            },
        ],
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.json())


api_response =call_openai_gpt(OPENAI_KEY, 'Escribe un breve poema sobre la programacion')
print(json.dumps(api_response, indent=4))


## Utilizando API de DeepSeek

DEEPSEEK_KEY = 'sk-xxxxxxx'


def call_deepseek(api_key, prompt):
    url = 'https://api.deepseek.com/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        "model": "deepseek-chat",
        "message": [
            {
                'role': 'user',
                'content': prompt
            },
        ],
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.json())


api_response =call_deepseek(DEEPSEEK_KEY, 'Escribe un breve poema sobre la programacion')
print(json.dumps(api_response, indent=4))

#https://platform.deepseek.com/api_keys
#https://platform.openai.com/docs/overview
