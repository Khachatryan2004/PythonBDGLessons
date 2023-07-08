import telebot
import webbrowser
from telebot import types
import sqlite3

bot = telebot.TeleBot('6095270561:AAGYkzGwT6Vo8AIm30G9fR3epK7n3tPlavs')
name = None


@bot.message_handler(commands=['start', 'Start'])
def start(message):
    # DataBase
    conn = sqlite3.connect('BotDataBase.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), pass VARCHAR(50))'
    )
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Enter your name for registration')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Enter Password')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    bot.register_next_step_handler(message, user_pass, name)
    password = message.text.strip()
    conn = sqlite3.connect('BotDataBase.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES ("%s", "%s")' % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('a list of users', callback_data='user'))
    bot.send_message(message.chat.id, 'Registered', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('BotDataBase.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Name: {el[1]}, password: {el[2]}\n'

    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
