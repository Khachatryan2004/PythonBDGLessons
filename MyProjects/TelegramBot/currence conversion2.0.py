import telebot
from forex_python.bitcoin import BtcConverter
from telebot import types
import requests

bot = telebot.TeleBot('6095270561:AAGYkzGwT6Vo8AIm30G9fR3epK7n3tPlavs')
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.register_next_step_handler(message, summa)

    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name:
        full_name = f'{first_name} {last_name}'
    else:
        full_name = first_name
    bot.send_message(message.chat.id, f'Hello {full_name}, ')


def summa(message):
    global amount
    try:
        amount = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Oops, something is wrong. Try again')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        button2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        button3 = types.InlineKeyboardButton('USD/AMD', callback_data='usd/amd')
        button4 = types.InlineKeyboardButton('Another', callback_data='else')
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, 'SELECT CURRENCY PAIR', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Number must be greater than 0! Try again')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'else':
        markup = types.InlineKeyboardMarkup(row_width=2)
        button5 = types.InlineKeyboardButton('USD/JPY', callback_data='usd/jpy')
        button6 = types.InlineKeyboardButton('EUR/GBP', callback_data='eur/gbp')
        button7 = types.InlineKeyboardButton('GBP/USD', callback_data='gbp/usd')
        button8 = types.InlineKeyboardButton('Back', callback_data='back')
        markup.add(button5, button6, button7, button8)
        bot.send_message(call.message.chat.id, 'SELECT ANOTHER CURRENCY PAIR', reply_markup=markup)
    elif call.data == 'back':
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        button2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        button3 = types.InlineKeyboardButton('USD/AMD', callback_data='usd/amd')
        button4 = types.InlineKeyboardButton('Another', callback_data='else')
        markup.add(button1, button2, button3, button4)
        bot.send_message(call.message.chat.id, 'SELECT CURRENCY PAIR', reply_markup=markup)
    else:
        values = call.data.upper().split('/')
        url = f'https://api.exchangerate-api.com/v4/latest/{values[0]}'
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][values[1]]
        res = amount * rate
        bot.send_message(call.message.chat.id, f'Value: {round(res, 2)}. You can re-enter the amount')
        bot.register_next_step_handler(call.message, summa)


bot.polling(none_stop=True)
