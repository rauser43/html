import pprint
import telebot
import time
import os

TOKEN='5552840171:AAF6JyZvsAoYSP-4ITCuCfXjfDieeLe8v8w'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'***{text.upper()}!***')

@bot.message_handler(commands=['start', 'help'])
def send_wellcome (message):
    bot.reply_to (message, "How are you?")

@bot.message_handler(commands=['timer'])
def timer(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)

@bot.message_handler(content_types=['text'])
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, "Содержит слово плохой")
        return
    text=message.text[::-1]
    bot.reply_to (message,text)

@bot.message_handler (content_types=['sticker'])
def send_sticker (message):
    FILE_ID = "107"
    bot.send_sticker(message.chat.id, FILE_ID)
# @bot.message_handler(content_types=commands= ['say'])
# def reverse_text(message):
bot.polling()

