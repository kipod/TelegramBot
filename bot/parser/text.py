from .message import Message


class Text(Message):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.bot.callback_query_handler(func=lambda call: True)
        def _callback_worker(call):
            self.callback(call)
