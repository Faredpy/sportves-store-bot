import requests
import telebot
from config import *
from sql import *
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if(message.text == '/start'):
        data = getCategory()
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row(*data.keys())
        keyboard.row('Назад')
        bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def start(message):
    idCat = categoryList[message.text]
    data = getProductInCategory(idCat)
    dataProducts = getProduct(data)
    for product in dataProducts:
        print(product)
        bot.send_message(message.from_user.id, 'Модель:' + product["model"] + '\n' 
        + 'Картинка:' + product["img"] + '\n' + 'Цена:' + product["price"])
    

bot.polling(none_stop=True, interval=0)
