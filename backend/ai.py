import requests
import base64

url = "https://api.getimg.ai/v1/latent-consistency/text-to-image"

payload = { 
        "prompt": "Dark forest and city from 300 year",
        "height": 1024,
        "width": 576,
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer key-2AJ60aySGbg40qcH58Ouk7bfQPPOuSDEkppsSilg0UpJZcVdQhAcarKwebhp6rny1s6XXTXez1RH0l7C6bH67zL1i4eDoiv8"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

img_data = response.json()['image']

with open("imageToSave.png", "wb") as fh:
    fh.write(base64.decodebytes(img_data.encode()))