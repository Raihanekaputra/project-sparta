import requests

api_key = 'f1b244da-d3d6-41f4-8214-83bd47ff45ff'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)