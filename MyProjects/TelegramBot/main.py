import telebot
import webbrowser
from telebot import types
import sqlite3

bot = telebot.TeleBot('6095270561:AAGYkzGwT6Vo8AIm30G9fR3epK7n3tPlavs')
name = None


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com/')



@bot.message_handler(commands=['start', 'Start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('My Instagram')
    markup.row(button1)
    bot.reply_to(message, 'I Came', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name:
        full_name = f"{first_name} {last_name}"
    else:
        full_name = first_name
    bot.send_message(message.chat.id, f'Hello, {full_name}')

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


def on_click(message):
    if message.text == 'My Instagram':
        bot.send_message(message.chat.id, 'Instagram is Opened')


@bot.message_handler(commands=['help', 'Help'])
def main(message):
    bot.send_message(message.chat.id, 'My help information is empty')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Go to my Instagram', url='https://www.instagram.com/')
    markup.row(button1)
    button2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    button3 = types.InlineKeyboardButton('Change text', callback_data='edit')
    markup.row(button2, button3)
    bot.reply_to(message, 'Cool photo', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)


