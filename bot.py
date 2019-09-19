import os

import telebot

from logger import log

BOT_TOKEN = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(BOT_TOKEN)
name = ''
surname = ''
age = 0


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    log(log.INFO, 'get_text_messages %s', message)
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет что бы поздороваться , "
                                               "или напиши /reg для того что бы я с тобой познакомился")
    elif message.text == "/reg":
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def get_name(message):
    log(log.INFO, 'get_name %s', message)
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    log(log.INFO, 'get_surname %s', message)
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    log(log.INFO, 'get_age %s', message)
    global age
    while age == 0:
        try:
            age = int(message.text)
        except ValueError:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = telebot.types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        ...
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        ...


bot.polling(none_stop=True, interval=0)
