import telebot
import json
import random

bot = telebot.TeleBot('830533878:AAFKl0RXgd0ZTmkHlK8R1QXNavj66iImxts')

with open('data.json', 'r+') as file:
    data = json.load(file)
    print(data)


@bot.message_handler(commands=['start'])
def send(message):
    try:
        bot.send_message(message.chat.id, random.randint(int(data['start']), int(data['end'])))
    except:
        bot.send_message(message.chat.id, ' Что-то пошло не так')

@bot.message_handler(commands=['config'])
def send(message):
    try:
        response = message.text
        print(response.split())
        data['start'] = response.split()[1]
        data['end'] = response.split()[2]
        with open('data.json', 'w') as f:
            dt = f.write(json.dumps(data))
            bot.send_message(message.chat.id, random.randint(int(data['start']), int(data['end'])))
    except:
        bot.send_message(message.chat.id, "Ты тупой или как?")

@bot.message_handler(content_types=['text'])
def send(message):
    bot.send_message(message.chat.id, 'Я тебя не понял')
if __name__ == '__main__':
    bot.polling(none_stop=True)
