from telebot import types
import json
import telebot
import codecs

token = '7088715543:AAE8PWST6q8j9EN_mC5gvvPNd9g3uhKyJBU'

bot = telebot.TeleBot(token)

def keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    two_butt = types.InlineKeyboardButton(text="Launch app", url="https://t.me/funk_ai_bot/start")
    keyboard.add(two_butt)
    return keyboard

fileObj = codecs.open( "./Hello.json", "r", "utf_8_sig" )
text = fileObj.read() # или читайте по строке
data = json.loads(text)
fileObj.close()

print(bot.get_me())

for item in data["objects"] [0] ["rows"]:
    try:
        print(item[1])
        photo = open('./photorealizm.png', 'rb')
        bot.send_photo(item[1], photo, '''
        Meet photorealism on FUNK AI. Image base becames bigger everyday!
        ''', reply_markup=keyboard())
    except:pass


#bot.infinity_polling()