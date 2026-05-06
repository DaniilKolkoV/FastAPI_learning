import requests

response = requests.get("https://api.github.com/users/этого_точно_нет_12345xyz")
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"Обнаружена ошибка {e}, при запросе {response.text}")
data = response.json()