import requests

res = requests.post('http://127.0.0.1:5000/user/me',json={'tg_id':100})
print(res.json())