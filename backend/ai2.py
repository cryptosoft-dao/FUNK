import json

with open('./data1.json','r') as f:
    img_data = json.load(f)['image']

import base64
with open("imageToSave.png", "wb") as fh:
    fh.write(base64.decodebytes(img_data.encode()))