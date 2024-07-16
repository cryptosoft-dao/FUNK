from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import create_engine, select, Column, Integer, String, Boolean

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    coins = Column(Integer, default = 0)
    coins_per_click = Column(Integer, default = 1)
    clicked_time = Column(Integer, default = 0)
    level_id = Column(Integer, default = 0)
class Ad(Base):
    __tablename__ = 'ads'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    decsription = Column(String)
    per_click = Column(Integer, default=1)
    url = Column(String)
    image = Column(String)

app = Flask(__name__)
cors = CORS(app)
engine = create_engine('sqlite:///server.db')

LEVELS = [
    {'id': 0, 'name': 'Новичок', 'coins': 0},
    {'id': 1, 'name': 'Новичок2', 'coins': 10},
    {'id': 2, 'name': 'Новичок3', 'coins': 20},
]

def init():
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@app.post('/user/me')
def user_me():
    data = request.get_json()
    with Session(engine) as session:
        user = session.execute(select(User).where(User.tg_id == data['tg_id'])).scalar()
        if user == None:
            user = User(tg_id = data['tg_id'])
            session.add(user)
            session.commit()
        
        level = list(filter(lambda l: l['id'] == user.level_id,LEVELS))[0]
        next_level = list(filter(lambda l: l['id'] == user.level_id + 1,LEVELS))[0]
        
        if next_level['coins'] - user.coins <= 0:
            user.level_id += 1
            session.commit()

        level = list(filter(lambda l: l['id'] == user.level_id,LEVELS))[0]
        next_level = list(filter(lambda l: l['id'] == user.level_id + 1,LEVELS))[0]
        
        return jsonify({
            'coins':user.coins,
            'coins_per_click':user.coins_per_click,
            'level_name':level['name'],
            'coins_to_new_level':next_level['coins'] - user.coins
        })    
@app.get('/ads/all')
def get_all_ads():
    ads = []
    with Session(engine) as session:
        all_ads = session.execute(select(Ad)).scalars().all()
    for ad in all_ads:
        ads.append({'id':ad.id, 'name':ad.name, 'description':ad.decsription, 'image':f"/ads/{ad.image}", 'per_click':ad.per_click, 'url':ad.url})
    return jsonify({'ads':ads})
@app.get('/ads/<image>')
def get_ad_image(image):
    return send_file(f'./ads/{image}')
if __name__ == '__main__':
    init()
    app.run(debug=True)