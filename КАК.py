# coding: utf-8
импортный  телебот
от  telebot  импортных  типов
бот  =  телебот . TeleBot ( '5042325777: AAG8CYZqT2c8tzr5xhcIo2ECAwa-rDUCLtc' )
first  = [ "Оплатить можно по карте. \ n Стоимость: 1мин. = 5руб. \ n Ожидание: 0,5руб." ]
second  = [ "Для начала нужно отсканировать QR_cod." ]

@ бот . message_handler ( content_types = [ 'текст' ])
def  get_text_messages ( сообщение ):
    если  сообщение . text  ==  "Привет" :
        бот . send_message ( message . from_user . id , "Привет, сейчас я расскажу тебе что нужно делать." )
        клавиатура  =  типы . InlineKeyboardMarkup ()
        key_oplata  =  типы . InlineKeyboardButton ( текст = 'Как заплатить?' , Callback_data = 'Vopros' )
        клавиатура . добавить ( key_oplata )
        key_poezd  =  типы . InlineKeyboardButton ( текст = 'Как поехать?' , Callback_data = 'вопр' )
        клавиатура . добавить ( key_poezd )
        бот . send_message ( message . from_user . id , text = 'Что тебя интересует?' , reply_markup = keyboard )
     сообщение elif . text  ==  "/ help" :
        бот . send_message ( сообщение . from_user . id , "Напиши Привет" )
    еще :
        бот . send_message ( message . from_user . id , "Я тебя не понимаю. Напиши / help." )

@ бот . callback_query_handler ( func = лямбда-  вызов : True )
def  callback_worker ( вызов ):
    если  звоните . data  ==  "вопрос" :
        msg  =  первый
        бот . send_message ( звонок . сообщение . чат . id , сообщение )
    elif  call . data  ==  "vopr" :
        мс  =  секунда
        бот . send_message ( звонок . сообщение . чат . id , мс )
бот . опрос ( none_stop = True , interval = 0 )

'''import requests
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
bot.polling(none_stop=True, interval=0)'''
