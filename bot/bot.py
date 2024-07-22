from telebot import types
import telebot
import requests

URL = 'https://funkai.ru'
TG_TOKEN = '7233254807:AAHwwz6mbVjLNNqFIm_U0ZnVQWvbCt0cTEc'
BASE_URL = 'https://funkai.online'
IMAGES_ID = []
def webAppKeyboard(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    image_id = 0
    print(IMAGES_ID)
    for img in IMAGES_ID:
        print(img)
        if img['tg_id'] == message.from_user.id:
            image_id = img['image_id']
            break
    print(image_id)
    webAppTest = types.WebAppInfo(f'{URL}?{image_id}?')
    one_butt = types.InlineKeyboardButton(text="Go! Go! Go!", web_app=webAppTest)
    two_butt = types.InlineKeyboardButton(text="Join FUNK community", url="https://t.me/funk_ai_chat")
    keyboard.add(one_butt, two_butt,row_width=2)

    return keyboard
def has_referrer(user_id):
    res = requests.post(f'{BASE_URL}/ref/has_ref',json={'tg_id':user_id})
    return res.json()['has_ref']
def get_all_users():
    data = requests.post(f'{BASE_URL}/users/all')
    return data.json()['users']
def add_ref(creator, come, has_tg_premium, user_name):
    requests.post(f'{BASE_URL}/ref/add',json={'creator_id':creator,'come_id':come, 'has_tg_premium':has_tg_premium, 'user_name':user_name})

bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    
    user_id = message.from_user.id
    if True:
        if " " in message.text:
            url_data = message.text.split()[1]
            referrer_candidate = url_data.split("-")[0]
            try:
                referrer_candidate = int(referrer_candidate)
                if user_id != referrer_candidate and referrer_candidate in get_all_users():
                    referer = referrer_candidate
                    has_tg_premium = message.from_user.is_premium
                    user_name = message.from_user.first_name
                    add_ref(referer, user_id, has_tg_premium, user_name)

            except ValueError as e:
                print('e: ',e)
                pass
            try:
                image_id = url_data.split('-')[1]
                for img in IMAGES_ID:
                    if img['tg_id'] == message.from_user.id:
                        img['image_id'] = image_id
                        break
                else:
                    IMAGES_ID.append({'tg_id':message.from_user.id,'image_id':image_id})
            except:
                pass
    photo = open('./main_image.png', 'rb')
    bot.send_photo(message.chat.id, photo, '''
Swipe content and get tokens!
''', parse_mode="html", reply_markup=webAppKeyboard(message))


bot.infinity_polling(skip_pending=False)
