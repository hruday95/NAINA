# st
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)



from bot_telegram.bot_class import TelegramBot



api.add_resource(TelegramBot, '/telegram')


if __name__ == '__main__':
    app.run(debug=True)




