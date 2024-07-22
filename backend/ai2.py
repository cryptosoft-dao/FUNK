import requests

for i in range(0,250):
    res = requests.post("https://hamster-dev.online/files/AI|a1a8a63004c91bf13ab3c9cd5bb60af9337e44966011d3dc4da06b73be32432b/add_without_prompt",json={},headers={
        'Content-Type': 'application/json'
    })
    print(f'{i} - {res.text}')