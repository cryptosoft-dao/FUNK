from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import create_engine, select, Column, Integer, String

import random
from random_prompt import RandomPromptGenerator

import requests
import base64

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    name = Column(String(255))
    image = Column(String(255))
    coins = Column(Integer, default = 0)
    coins_per_click = Column(Integer, default = 1)
    clicked_time = Column(Integer, default = 0)
    level_id = Column(Integer, default = 0)
class Ad(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    decsription = Column(String(255))
    per_click = Column(Integer, default=1)
    url = Column(String(255))
    image = Column(String(255))
class Ref(Base):
    __tablename__ = 'refs'

    id = Column(Integer, primary_key=True)

    creator_id = Column(Integer)
    come_id = Column(Integer)

app = Flask(__name__)
cors = CORS(app)
AI_KEY = "key-3gu9q47JEsxOGDOdr1T14G6zK4EDHLtR4aSmmbOJIxaSNTccGY0vS4hMb3Yhh43VEbxxYQl7I9gTU7GoT1C4gqBNJTENIVp4"
PROMPT_GENERATOR = RandomPromptGenerator()

user = 'u2745068_admin'
password = 'admin123'
host = 'server18.hosting.reg.ru'
port = 3306
database = 'u2745068_main'

engine = create_engine(
   'sqlite:///server.db'
)
#url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
# "mysql+pymysql://u2513925_admin:Vadim234@server149.hosting.reg.ru:1500//u2513925_hamsterdevonline"
LEVELS = [
    {'id': 0, 'name': 'Новичок', 'coins': 0},
    {'id': 1, 'name': 'Новичок2', 'coins': 10},
    {'id': 2, 'name': 'Новичок3', 'coins': 20},
]

def init():
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
def convert_moneys(money: int):
    money_str = str(money)
    if money >= 100: money_str = f'{money / 1000}K' #0.5K 10K
    if money >= 100_000: money_str = f'{money / 1_000_000}M'
    if money >= 100_000_000: money_str = f'{money / 1_000_000_000}B'

    return money_str
def add_ai(prompt:str, imagePath: str):
    url = "https://api.getimg.ai/v1/latent-consistency/text-to-image"

    payload = {
        "prompt": prompt,
        "height": 1024,
        "width": 576,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {AI_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())

    img_data = response.json()['image']

    with open(imagePath, "wb") as fh:
        fh.write(base64.decodebytes(img_data.encode()))
@app.post('/user/me')
def user_me():
    try:
        data = request.get_json()
        with Session(engine) as session:
            user = session.execute(select(User).where(User.tg_id == data['tg_id'])).scalar()
            if user == None:
                user = User(tg_id = data['tg_id'],name = data['name'],image = 'none')
                session.add(user)
                session.commit()

            return jsonify({
                'coins':user.coins,
                'coins_per_click':user.coins_per_click,
                'converted_coins':convert_moneys(user.coins)
            })
    except Exception as e:
        return jsonify({'e':e})
@app.post("/users/all")
def get_all_users():
    with Session(engine) as session:
        tgs_all = session.execute(select(User)).scalars().all()
        tgs = list(map(lambda l: l.tg_id, tgs_all))
        return jsonify({'users':tgs})
@app.post('/user/swipe')
def user_swipe():
    data = request.get_json()
    with Session(engine) as session:
        user = session.execute(select(User).where(User.tg_id == data['tg_id'])).scalar()
        if user == None:
            return jsonify({'status':400})
        user.coins += 1
        user.clicked_time += 1
        session.commit()

        return jsonify({'status': 200, 'coins':user.coins})
@app.post('/ads/all')
def get_all_ads():
    try:
        ads = []
        start_id = request.get_json().get('startId',0)
        with Session(engine) as session:
            all_ads = session.execute(select(Ad)).scalars().all()
        for ad in all_ads:
            ads.append({'id':ad.id, 'name':ad.name, 'description':ad.decsription, 'image':f"/ads/image/{ad.image}", 'per_click':ad.per_click, 'url':ad.url})
        random.shuffle(ads)
        for ad in ads:
            if ad['id'] == start_id:
                filtered_list = list(filter(lambda l: l['id'] != start_id, ads))
                final_ads = [ad, *filtered_list]
                break
        else:
            final_ads = [*ads]
        return jsonify({'ads':final_ads})
    except Exception as e:
        return jsonify({'status':400, 'error':str(e)})
@app.get('/ads/image/<image>')
def get_ad_image(image):
    return send_file(f'./ads/{image}')
@app.post("/ref/all")
def get_all_refs():
    data = request.get_json()
    refs = []
    with Session(engine) as session:
        res = session.execute(select(Ref).where(Ref.creator_id == data['tg_id'])).scalars().all()
        for f in res:
            u = session.execute(select(User).where(User.tg_id == f.come_id)).scalar()
            print(u.tg_id)
            total_friends_1 = session.execute(select(Ref).where(Ref.creator_id == u.tg_id)).scalars().all()
            print(total_friends_1)
            total_friends = len(total_friends_1)
            refs.append({
                'name':u.name,
                'money':u.coins,
                'total_friends':total_friends,
                'converted_coins':convert_moneys(u.coins),
                'image':u.image
            })
    return jsonify({'refs':refs})
@app.get("/test_data/image")
def get_test_image():
    return send_file("./test_data/image.png")
@app.post("/ref/add")
def add_ref():
    data = request.get_json()
    print(data)
    with Session(engine) as session:
        ref = session.execute(select(Ref).where(Ref.creator_id == data['creator_id'], Ref.come_id == data['come_id'])).scalar()
        print(ref)
        if ref == None:
            ref = Ref(creator_id = data['creator_id'], come_id = data['come_id'])
            session.add(ref)
            session.commit()
        return jsonify({'status':200})
@app.get('/server/a')
def get_server():
    return  send_file('./server.db')
@app.post('/files/AI|a1a8a63004c91bf13ab3c9cd5bb60af9337e44966011d3dc4da06b73be32432b/add_with_prompt')
def add_ai_image_with_prompt():
    data = request.get_json()
    print(data)
    print(data['prompt'])
    with Session(engine) as session:
        ad = Ad(name=data.get('name',''), decsription=data.get('decsription',''), url=data.get('url',''),image='')
        session.add(ad)
        session.commit()
        ad_id = ad.id
        add_ai(data['prompt'], f'./ads/{ad_id}.png')
        ad.image = f'{ad_id}.png'

        session.commit()

        return jsonify({'status':200, 'image':f'/ads/image/{ad_id}.png'})

@app.post('/files/AI|a1a8a63004c91bf13ab3c9cd5bb60af9337e44966011d3dc4da06b73be32432b/add_without_prompt')
def add_ai_image_without_prompt():
    data = request.get_json()
    print(data)
    data['prompt'] = PROMPT_GENERATOR.random_prompt()
    with Session(engine) as session:
        ad = Ad(name=data.get('name',''), decsription=data.get('decsription',''), url=data.get('url',''),image='')
        session.add(ad)
        session.commit()
        ad_id = ad.id
        add_ai(data['prompt'], f'./ads/{ad_id}.png')
        ad.image = f'{ad_id}.png'

        session.commit()

        return jsonify({'status':200, 'image':f'/ads/image/{ad_id}.png'})


if __name__ == '__main__':
    init()
    app.run(debug=True,port=8080)