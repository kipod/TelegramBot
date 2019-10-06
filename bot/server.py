import telebot
from bot.config import CONFIG
from .parser import Text, Photo
from logger import log

class Server:
    def __init__(self):
        self.bot = telebot.TeleBot(CONFIG.bot_token)
        self.handler = {
            'text': Text(self.bot),
            'photo': Photo(self.bot)
        }

        @self.bot.message_handler(content_types=['text', 'photo'])
        def _get_text_messages(message):
            log(log.INFO, "received [%s]", message.content_type)
            self.handler[message.content_type].message(message)

        @self.bot.edited_message_handler(content_types=['text', 'photo'])
        def _on_edited_message(message):
            self.handler[message.content_type].edited_message(message)

        # noinspection PyUnusedLocal
        @self.bot.channel_post_handler(content_types=['text', 'photo'])
        def __handler(*args, **kwargs):
            log(log.WARNING, '>>>channel_post<<<')

        # noinspection PyUnusedLocal
        @self.bot.edited_channel_post_handler(content_types=['text', 'photo'])
        def __handler(*args, **kwargs):
            log(log.WARNING, '>>>edited_channel_post<<<')

        # noinspection PyUnusedLocal
        @self.bot.inline_handler
        def __handler(*args, **kwargs):
            log(log.WARNING, '>>>inline<<<')

        # noinspection PyUnusedLocal
        @self.bot.chosen_inline_handler
        def __handler(*args, **kwargs):
            log(log.WARNING, '>>>chosen_inline<<<')

        # noinspection PyUnusedLocal
        @self.bot.callback_query_handler
        def __handler(*args, **kwargs):
            log(log.WARNING, '>>>callback_query<<<')

        # noinspection PyUnusedLocal
        @self.bot.shipping_query_handler
        def __handler(*args, **kwargs):
            log(log.WARNING, '>>>shipping_query<<<')

        # noinspection PyUnusedLocal
        @self.bot.pre_checkout_query_handler
        def __handler(*args, **kwargs):
            log(log.WARNING, '>>>pre_checkout_query<<<')

    def run(self):
        log(log.INFO, 'starting bot server... ')
        me = self.get_me()
        for attr in me:
            log(log.INFO, "%s: %s", attr, me[attr])
        self.bot.polling(none_stop=True, interval=0)

    def get_me(self):
        me = self.bot.get_me()
        attributes = [a for a in dir(me) if not a.startswith('_') and not callable(getattr(me, a))]
        return {a: getattr(me, a) for a in attributes}
