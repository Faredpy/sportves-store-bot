import requests
import telebot
from config import *
from telebot import types
from sql import *

bot = telebot.TeleBot(TOKEN)
categiry = []


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if(message.text == '/start'):
        btnNames = []
        data = connect_db('getCategory')
        for category in data:
            btnNames.append(category.name)

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(*btnNames)
        msg = bot.reply_to(message, 'Какой товар интересует',
                           reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)


def process_step(message):
    if message.text == '1':
        bot.send_message(message.from_user.id, 'Ответ на 1')
    else:
        print('1222')


@bot.message_handler(content_types=['text'])
def start(message):
    if(message != '/start'):
        bot.send_message(message.from_user.id, 'Нажми /start')


bot.polling(none_stop=True, interval=0)
