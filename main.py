import random
from telebot import types
from bots_data import bot


def create_password():
    password = []
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
    final = ''.join(map(str, password))
    return final


@bot.message_handler(commands=['start'])
def start(message):
    print('new user')
    markup = types.ReplyKeyboardMarkup(True)
    markup.row('Generate password')
    bot.send_message(message.chat.id, 'Hello there. I am not Obivan Kenobe, but anyway...', reply_markup=markup)


@bot.message_handler(commands=['help'])
def helping(message):
    if random.randint(0, 1) == 0:
        bot.send_message(message.chat.id, 'no one will help you')
    else:
        bot.send_message(message.chat.id, 'are you scare?')


@bot.message_handler(content_types=['text'])
def welcome_text(message):
    if message.chat.type == 'private':
        if message.text == 'Generate password':
            bot.send_message(message.chat.id, create_password())


while True:
    try:
        bot.polling(non_stop=True, interval=1)
    except(ConnectionAbortedError, ConnectionError, ConnectionResetError, ConnectionRefusedError):
        break
