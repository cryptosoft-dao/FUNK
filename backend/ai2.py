import requests
from pprint import pprint
import time
headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer 1721199341753MDmINM2v2G4caUbqyXJfkuSB7A1RTedfOQmApbPk418lrCkcTA96nmJs7iP5R6n36742056004',
    'content-type': 'application/json',
    'origin': 'https://hamsterkombatgame.io',
    'priority': 'u=1, i',
    'referer': 'https://hamsterkombatgame.io/',
    'sec-ch-ua': '"Opera";v="111", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
}

json_data = {
    'count': 7000,
    'availableTaps': 0,
    'timestamp': round(time.time()),
}

response = requests.post('https://api.hamsterkombatgame.io/clicker/tap', headers=headers, json=json_data)
pprint(response.json())