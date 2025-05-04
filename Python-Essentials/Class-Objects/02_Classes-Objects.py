#1. Introduccion a las Classes de Python
# De forma simplificada, son plantillas para crear objetos
# Un objeto es una instancia de una clase.


# Permite agrupar datos(atributos o propiedades) y funciones (metodos) en un solo lugar

class Coche:
    #Atributo de clase(comparte todas las instancias)
    tipo = 'vehiculo de cuatro ruedas'

    # Metodo especial que es le que construye el objeto
    # Al llamar a la clase
    # Se llama automaticamente este metodo cuando creas la instancia.

    def __init__(self, marca, modelo, color):  # el self se refiere a si mimso
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f'EL coche {self.marca} {self.modelo} ha arrancado')


carro1 = Coche('ford', 'mustang', 'rojo')
carro2 = Coche('fiat', 'punto', 'blanco')

carro1.arrancar()
carro2.arrancar()

#Encapsulacion: es ocultar los detalles internos de una clase y exponer solo la interfaz publica


import os

# Crear una clase para llamar a la API de OpenAI, DeepSeek o lo que sea
import requests


class API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'model': self.model,
            'message': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        }
        response = requests.post(self.url, json=data, headers=headers)
        print(response.json())
        res_json = response.json()
        print(res_json['choices'][0]['message']['content'])


open_ai_api = API(os.getenv('OPENAI_API_KEY'), 'https://api.openai.com/v1/chat/completions', 'gpt-4o-mini')
open_ai_api.call('Escribe un breve poema sobre la programacion')

