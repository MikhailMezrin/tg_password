import random
import telebot
from telebot import types
password = []
bot = telebot.TeleBot('5461610581:AAFyTqSB6b0WZcLsuMjQywSvC_Op3Fc65QU')


def create_password():
    for i in range(15):
        type_char = random.randint(0, 3)
        if type_char == 0:
            password.append(random.randint(0, 10))
        elif type_char == 1:
            password.append(chr(random.randint(97, 123)))
        elif type_char == 2:
            password.append(chr(random.randint(65, 91)))
        elif type_char == 3:
            password.append(chr(random.randint(33, 65)))
    return ''.join(map(str, password))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('generate password')

    markup.add(button)


@bot.message_handler(commands=['text'])
def send_password(message):
    if message.chat.type == 'private':
        if message.text == 'start':
            bot.send_message(message.chat.id, 'hello there')
        if message.text == 'generate password':
            bot.send_message(message.chat.id, create_password())


while True:
    bot.polling(non_stop=True, interval=1)
# print(''.join(map(str, password)))
