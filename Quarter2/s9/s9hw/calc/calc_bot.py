import telebot
from datetime import datetime


API_TOKEN = 'there is the token'
bot = telebot.TeleBot(API_TOKEN)


def log(message):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}: {message.text}\n')


@bot.message_handler(commands='/calc')
def calc(message):
    log(message)
    res = eval(" ".join(message.text.split()[1:]).replace(',', '.'))
    bot.send_message(message.chat.id, f'Result is: {res}')


@bot.message_handler(commands='/log')
def show_log(message):
    with open('log.txt', 'r', encoding='utf-8') as f:
        out = str(f.read())
        bot.send_message(message.chat.id, out)


bot.polling()
