import requests

TOKEN = '613756f8efd7225b9121f6cdf53b5e39'
URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
ID_Pokemon = '65960'

body_create = {
    "name": "Мьюшка",
    "photo_id": 15
}

body_in_pokeball = {
    "pokemon_id": ID_Pokemon
}

body_name = {
    "pokemon_id": ID_Pokemon,
    "name": "Мьюшка",
    "photo_id": 150
}



response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)


respone_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_in_pokeball)
print(respone_in_pokeball.text)

respone_in_pokeball = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(respone_in_pokeball.text)
