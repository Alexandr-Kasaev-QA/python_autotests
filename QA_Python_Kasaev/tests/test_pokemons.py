import requests
import pytest

TOKEN = '613756f8efd7225b9121f6cdf53b5e39'
URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
ID_Pokemon = '65960'
LEVEL = {'level' : 5}
Trainer_ID = {'trainer_id' : 4826}



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = LEVEL)
    assert response.status_code == 200


def test_part_name():
    response = requests.get(url = f'{URL}/trainers', params = Trainer_ID)
    assert response.json()["data"][0]["trainer_name"] == 'destro'