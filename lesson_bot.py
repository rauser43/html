import pprint
import telebot
import time
import os

# файл дляпарсинга данных
from code import parse

TOKEN='5552840171:AAF6JyZvsAoYSP-4ITCuCfXjfDieeLe8v8w'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = message.text.split()[1]
    bot.reply_to(message, text[::-1])

@bot.message_handler(commands=['parse'])
def parse_site (message):
    text = message.text.split()[1]
    chat_id = message.chat.id
    q = parce(text)
    for it in q[:20]:
        bot.send_message(chat_id, f'{it[0]} - {it[1]}')

@bot.message_handler(commands=['file'])
def send_file(message):
    chat_id = message.chat.id
    if exists('base.csv'):
        with open('base.csv') as f:
            bot.send_document(chat_id, f)
    else:
        bot.send_message(chat_id, 'Файл не сформирован. Используйте команду /parce для его формирования')

@bot.message_handler(func=lambda m: True)
def echo(message):
    print(message)
    bot.reply_to(message, message.text.upper())


bot.infinity_polling()