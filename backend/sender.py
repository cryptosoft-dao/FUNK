from telebot import types
import json
import telebot

token = '7194502673:AAEk2mq9vkmZncd7luD1t7tSh1UoEJEPHhU'
#token = '7233254807:AAHwwz6mbVjLNNqFIm_U0ZnVQWvbCt0cTEc' #FUNK

bot = telebot.TeleBot(token)
import codecs

def keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    two_butt = types.InlineKeyboardButton(text="Launch app", url="https://t.me/funk_ai_bot?start=7074103743-258")
    keyboard.add(two_butt)
    return keyboard

fileObj = codecs.open( "./tonclout.json", "r", "utf_8_sig" )
text = fileObj.read() # или читайте по строке
data = json.loads(text)
fileObj.close()

#for item in data['leaders']:
#    try:print(item['meta']['id'])
#    except:pass
photo = open('./main_image.png', 'rb')
bot.send_photo(238211251,photo,'''
🚀 RELEASE!

We are happy to announce FUNK! Click or swipe content to get rewards.

A Clicker Beneficiaries in stake!
''',reply_markup=keyboard())
print(bot.get_me())

#bot.infinity_polling()