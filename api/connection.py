import requests

response = requests.get("https://rickandmortyapi.com/api/character")
responseJson = response.json()
elapsed_time = response.elapsed.total_seconds()