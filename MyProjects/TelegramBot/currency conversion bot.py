import telebot
from currency_converter import CurrencyConverter
from telebot import types


bot = telebot.TeleBot('6095270561:AAGYkzGwT6Vo8AIm30G9fR3epK7n3tPlavs')
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello,enter the amount')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Oops, something is wrong try again')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        button2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        button3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        button4 = types.InlineKeyboardButton('Another', callback_data='else')
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, 'SELECT CURRENCY PAIR', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Number must be greater than 0!!, Try again')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Value: {round(res, 2)}.You can re-enter the amount')
        bot.register_next_step_handler(call.message, summa)

    else:
        bot.send_message(call.message.chat.id, 'Enter a couple of values separated by a slash')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Value: {round(res, 2)}. You can re-enter the amount')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Something is wrong, try again')
        bot.register_next_step_handler(message, my_currency)


bot.polling(none_stop=True)
