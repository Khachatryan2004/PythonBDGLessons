import telebot

bot = telebot.TeleBot('6095270561:AAGYkzGwT6Vo8AIm30G9fR3epK7n3tPlavs')
api = 'b1c9fcc42b2469d04bdd82fb794c4f6b'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, write the name of the city')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()


bot.polling(none_stop=True)
