import requests
import telebot
from telebot import types
bot = telebot.TeleBot('5042325777:AAG8CYZqT2c8tzr5xhcIo2ECAwa-rDUCLtc')
first = ["Оплатить можно по карте.\n Стоимость: 1мин.=5руб.\n Ожидание: 0,5руб."]
second = ["Для начала нужно отсканировать QR_cod."]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе что нужно делать.")
        keyboard = types.InlineKeyboardMarkup()
        key_oplata = types.InlineKeyboardButton(text='Как заплатить?', callback_data='tariffs')
        keyboard.add(key_oplata)
        key_poezd = types.InlineKeyboardButton(text='Как поехать?', callback_data='vopr')
        keyboard.add(key_poezd)
        bot.send_message(message.from_user.id, text='Что тебя интересует?', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "vopros": 
        msg = t
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "vopr":
        ms = second
        bot.send_message(call.message.chat.id, ms)
bot.polling(none_stop=True, interval=0)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Оплата":
        def tariffs():
            url = 'https://uram.ddns.net/uram_bot/tariffs'
            req_j = requests.get(url)
            req_data = req_j.json()
            if req_j.status_code == 200:
                try:
                    for req_data['tariffs'][0] in req_data['tariffs']:
                        bot.send_message(message.from_user.id, 'Цена: ' + str(req_data['tariffs'][5]['cost_minute']) +
                                         '\nНачало: ' + req_data['tariffs'][30]['cost_start'])
                except KeyError:
                    print('Что то пошло не так')
                except IndexError:
                    print()
            else:
                print('Что то пошло не так')
                t = tariffs()
bot.polling(none_stop=True, interval=0)
