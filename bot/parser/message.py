import telebot
from logger import log


class Message(object):
    def __init__(self, bot):
        self.bot = bot
        self.name = ''
        self.surname = ''
        self.age = 0

    def message(self, message):
        log(log.INFO, 'get_text_messages %s', message.text)
        if message.text == "Привет":
            self.bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            self.bot.send_message(message.from_user.id, "Напиши привет что бы поздороваться , "
                                                        "или напиши /reg для того что бы я с тобой познакомился")
        elif message.text == "/reg":
            self.bot.send_message(message.from_user.id, "Как тебя зовут?")
            self.bot.register_next_step_handler(message, self.__get_name)
        else:
            self.bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    def __get_name(self, message):
        log(log.INFO, 'get_name %s', message.text)
        self.name = message.text
        self.bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
        self.bot.register_next_step_handler(message, self.__get_surname)

    def __get_surname(self, message):
        log(log.INFO, 'get_surname %s', message.text)
        self.surname = message.text
        self.bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        self.bot.register_next_step_handler(message, self.__get_age)

    def __get_age(self, message):
        log(log.INFO, 'get_age %s', message.text)
        while self.age == 0:
            try:
                self.age = int(message.text)
            except ValueError:
                log(log.WARNING, 'age_is_not_int %s', message.text)
                self.bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
                self.bot.register_next_step_handler(message, self.__get_age)
                return
            keyboard = telebot.types.InlineKeyboardMarkup()
            log(log.INFO, 'inline_keyboard_button')
            key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='yes')
            keyboard.add(key_yes)
            key_no = telebot.types.InlineKeyboardButton(text='Нет', callback_data='no')
            keyboard.add(key_no)
            question = 'Тебе ' + str(self.age) + ' лет, тебя зовут ' + self.name + ' ' + self.surname + '?'
            self.bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    def callback(self, call):
        if call.data == "yes":
            self.bot.send_message(call.message.chat.id, 'Запомню : )')
            log(log.INFO, 'registration_complete')
        # elif call.data == "no":
        #     pass

    def edited_message(self, message):
        log(log.INFO, 'edited message id:%d', message.message_id)

