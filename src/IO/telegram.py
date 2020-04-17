import requests
from bottle import Bottle, response, request as bottle_request


class TelegramIO(Bottle):
    BOT_URL = 'https://api.telegram.org/bot1043633896:AAGTiCkJ_J_v9tNkDTBHGbkNCuGr12I9FUE/'
    message_url = BOT_URL + 'sendMessage'

    def __init__(self, data):
        self.data = data

    def run_reply(self):
        self.param_extractor()
        self.pass_to_engine()
        self.send_reply_to_user()

    def pass_to_engine(self):
        self.reply_from_engine = "reply from engine"

    def param_extractor(self):
        self.chat_id = self.data['message']['chat']['id']
        self.message_text = self.data['message']['text']
        self.sender_name = self.data['message']['from']['first_name']

    def send_reply_to_user(self):
        answer = "Hello " + self.sender_name + "\n\n\n From NAINA"
        json_data = {
            "chat_id": self.chat_id,
            "text": answer,
        }
        return requests.post(self.message_url, json=json_data)
